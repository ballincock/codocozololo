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

profile_handlers = Blueprint('profile_handlers', __name__)

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

@profile_handlers.before_request
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

@profile_handlers.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    user_id = session.get('user_id')
    
    if request.method == 'POST':
        db = get_db()
        cursor = db.cursor()
        
        display_name = request.form.get('display_name')
        bio = request.form.get('bio')
        social_media = request.form.get('social_media')
        
        cursor.execute(
            "UPDATE users SET display_name=%s, bio=%s, social_media=%s WHERE id=%s", 
            (display_name, bio, social_media, user_id)
        )
        db.commit()
        db.close()
        
        return redirect(url_for('index', mode='view'))

    return redirect(url_for('index', mode='view'))

@profile_handlers.route('/update_security', methods=['POST'])
def update_security():
    user_id = session.get('user_id')
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE users SET email=%s, backup_email=%s, mnemonic=%s WHERE id=%s", 
                   (request.form['email'], request.form['backup_email'], request.form['mnemonic'], user_id))
    db.commit()
    db.close()
    return redirect(url_for('index', mode='security'))

@profile_handlers.route('/upload_profile_pic', methods=['POST'])
def upload_profile_pic():
    print("Step 1: Route reached!")
    
    if 'file' not in request.files:
        print("Error: No file part in request")
        return redirect(url_for('profile'))
    
    file = request.files['file']
    if file.filename == '':
        print("Error: No selected file")
        return redirect(url_for('profile'))

    if file:
        try:
            filename = secure_filename(f"user_{session.get('user_id')}_{file.filename}")
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)
            print(f"Step 2: File saved to {save_path}")

            db = get_db()
            cursor = db.cursor()
            cursor.execute("UPDATE users SET profile_pic = %s WHERE id = %s", 
                           (filename, session.get('user_id')))
            db.commit()
            cursor.close()
            db.close()
            print("Step 3: Database updated!")

        except Exception as e:
            print(f"CRASH ERROR: {e}")
            return f"The server crashed: {e}"

    print("Step 4: Redirecting...")
    return redirect(url_for('update_profile'))
