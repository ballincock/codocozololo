from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL
from urllib.parse import quote
from datetime import datetime
from decimal import Decimal
import numpy.typing as npt
import mysql.connector
import requests
import warnings
import joblib4
import secrets
import math
import json
import os

chat = Blueprint('chat', __name__)

@staticmethod
def get_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pyrb",
            buffered=True
        )
    except mysql.connector.Error as err:
        print(f"DATABASE ERROR: {err}")
        return None

@chat.before_request
def load_logged_in_user():
    user = g.get('user')
    current_user_id = user['id'] if user else None
    if current_user_id is None:
        g.user = None
    else:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        g.user = cursor.fetchone()
        cursor.close()

@chat.route('/chat/<receiver>')
def chat_system(receiver):
    raw_user_val = session.get('user_id') 
    if not raw_user_val:
        return "No session found. Please log in through the main site.", 401
        
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT username FROM users WHERE id = %s OR username = %s", (raw_user_val, raw_user_val))
    user_row = cursor.fetchone()
    if not user_row:
        return "User not found in database.", 404
    active_user = user_row[0]

    cursor.execute("UPDATE messages SET is_read = TRUE WHERE sender_username = %s AND receiver_username = %s", (receiver, active_user))
    db.commit()

    cursor.execute("""
        SELECT DISTINCT IF(sender_username = %s, receiver_username, sender_username)
        FROM messages WHERE sender_username = %s OR receiver_username = %s
    """, (active_user, active_user, active_user))
    
    inbox_list = []
    for (name,) in cursor.fetchall():
        cursor.execute("SELECT COUNT(*) FROM messages WHERE sender_username = %s AND receiver_username = %s AND is_read = FALSE", (name, active_user))
        unread = cursor.fetchone()[0]
        inbox_list.append({'name': name, 'new': unread})

    cursor.execute("""
        SELECT id, sender_username, content FROM messages 
        WHERE ((sender_username=%s AND receiver_username=%s) 
           OR (sender_username=%s AND receiver_username=%s))
           AND is_deleted = FALSE ORDER BY timestamp ASC
    """, (active_user, receiver, receiver, active_user))
    
    message_data = []
    for (mid, sender, content) in cursor.fetchall():
        message_data.append({"id": mid, "sender": sender, "content": content})
    
    db.close()
    return render_template('chat.html', inbox=inbox_list, messages=message_data, receiver=receiver, current_user=active_user)

@chat.route('/api/send', methods=['POST'])
def send_msg():
    data = request.json
    db = get_db(); cursor = db.cursor()
    cursor.execute("SELECT username FROM users WHERE id = %s OR username = %s", (session['user_id'], session['user_id']))
    active_user = cursor.fetchone()[0]

    cursor.execute("INSERT INTO messages (sender_username, receiver_username, content) VALUES (%s, %s, %s)", 
                   (active_user, data['receiver'], data['content']))
    db.commit() 
    db.close()
    return jsonify({"status": "sent"})

@chat.route('/api/delete', methods=['POST'])
def delete_msg():
    data = request.json
    db = get_db(); cursor = db.cursor()
    cursor.execute("UPDATE messages SET is_deleted=TRUE WHERE id=%s", (data['id'],))
    db.commit(); db.close()
    return jsonify({"status": "deleted"})

@chat.route('/api/search_users')
def search_users():
    q = request.args.get('q', '').strip()
    active_user_id = session.get('user_id')
    
    if not q or not active_user_id:
        return jsonify([])

    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT username FROM users WHERE id = %s OR username = %s", (active_user_id, active_user_id))
    active_row = cursor.fetchone()
    active_name = active_row[0] if active_row else None

    cursor.execute("SELECT username FROM users WHERE username LIKE %s AND username != %s LIMIT 10", (f"%{q}%", active_name))
    
    results = [row[0] for row in cursor.fetchall()]
    
    db.close()
    return jsonify(results)
