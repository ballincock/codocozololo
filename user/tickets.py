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

tickets = Blueprint('tickets', __name__)

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

@tickets.before_request
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

@tickets.route('/tickets', methods=['GET', 'POST'])
def view_user_support_tickets():
    uid = session.get('user_id')
    if not uid: return redirect('/')

    db = get_db()
    cursor = db.cursor(dictionary=True)

    if request.method == 'POST':
        cursor.execute("INSERT INTO tickets (user_id, subject, message) VALUES (%s, %s, %s)", 
                       (uid, request.form.get('subject'), request.form.get('message')))
        db.commit()
        return redirect('/tickets')

    cursor.execute("SELECT * FROM tickets WHERE user_id = %s ORDER BY id DESC", (uid,))
    data_for_html = cursor.fetchall() 
    
    cursor.close()
    db.close()
    return render_template('tickets.html', tickets=data_for_html)

@tickets.route('/admin/tickets')
def admin_control():
    user_id = session.get('user_id')
    print(f"DEBUG: Admin accessing with ID: {user_id}") 
    
    if user_id != 1:
        return "Access Denied: Only User 1", 403

    db = get_db()
    cursor = db.cursor(dictionary=True) 
    
    cursor.execute("""
        SELECT t.*, u.username 
        FROM tickets t 
        LEFT JOIN users u ON t.user_id = u.id 
        ORDER BY t.id DESC
    """)
    admin_tickets = cursor.fetchall()
    
    cursor.close()
    db.close()
    return render_template('admin_control.html', tickets=admin_tickets)

@tickets.route('/admin/tickets/resolve/<int:ticket_id>')
def resolve_ticket(ticket_id):
    if session.get('user_id') != 1:
        return "Unauthorized", 401
    
    db = get_db()
    cursor = db.cursor()
    
    try:
        print(f"DEBUG: Attempting to resolve ticket ID: {ticket_id}")
        cursor.execute("UPDATE tickets SET status = 'Resolved' WHERE id = %s", (ticket_id,))
        
        db.commit() 
        print("DEBUG: Status updated successfully.")
        
    except Exception as e:
        print(f"DEBUG ERROR: {e}")
        return str(e), 500
        
    finally:
        cursor.close()
        db.close()
    return redirect('/admin/tickets')

@tickets.route('/admin/tickets/delete/<int:ticket_id>')
def delete_admin_ticket(ticket_id):
    if session.get('user_id') != 1:
        return "Unauthorized", 401
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM tickets WHERE id = %s", (ticket_id,))
    db.commit()
    cursor.close()
    db.close()
    return redirect(url_for('admin_control'))
