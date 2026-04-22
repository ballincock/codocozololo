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

authentication = Blueprint('authentication', __name__)

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

@authentication.before_request
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

@authentication.route('/auth', methods=['POST'])
def auth():
    try:
        d = request.json
        db = get_db()
        cursor = db.cursor(dictionary=True)
        
        if d.get('mode') == 1:  
            username = d.get('username')
            email = d.get('email')
            password = d.get('password')
            sq = d.get('securityquestion', 'What is your favorite color?')
            sa = d.get('securityanswer', '')
            
            p_hash = generate_password_hash(password)
            sa_hash = generate_password_hash(sa)
            
            mnemonic = " ".join(secrets.choice(["reef", "tide", "hook", "lure", "wave"]) for _ in range(12))
            
            cursor.execute(
                "INSERT INTO users (username, email, password, security_question, security_answer, mnemonic) VALUES (%s,%s,%s,%s,%s,%s)", 
                (username, email, p_hash, sq, sa_hash, mnemonic)
            )
            db.commit()
            
            session['user_id'] = cursor.lastrowid
            return jsonify({'status': 'success', 'mnemonic': mnemonic})
        
        else:
            username = d.get('username')
            password = d.get('password')
            
            cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
            user = cursor.fetchone()
            
            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                return jsonify({'status': 'success'})
            
            return jsonify({'status': 'error', 'error': 'Invalid credentials'}), 401
        
    except Exception as e:
        print(f"Error: {e}") 
        return jsonify({'status': 'error', 'error': str(e)}), 500

@authentication.route('/')
def index():
    user_id = session.get('user_id')
    mode = request.args.get('mode', 'dashboard' if user_id else 'auth')
    
    user = None
    if user_id:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        db.close()
    
    return render_template('index.html', mode=mode, user=user)
 
@authentication.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index', mode='auth'))
