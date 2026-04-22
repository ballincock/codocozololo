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

resets = Blueprint('resets', __name__)

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

@resets.before_request
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

@resets.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        mnemonic = request.form.get('mnemonic')
        db = get_db()
        cursor = db.cursor(dictionary=True)

        if mnemonic:
            cursor.execute("SELECT email FROM users WHERE mnemonic = %s", (mnemonic,))
            user = cursor.fetchone()
            if user:
                token = serializer.dumps(user['email'], salt='password-reset-salt')
                return redirect(url_for('reset_password', token=token))
                
            flash("Invalid mnemonic phrase.", "danger")
        
        elif email:
            cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
            if cursor.fetchone():
                token = serializer.dumps(email, salt='password-reset-salt')
                reset_url = url_for('reset_password', token=token, _external=True)
                msg = Message('Password Reset', sender='your-email@gmail.com', recipients=[email])
                msg.body = f'Reset link: {reset_url}'
                mail.send(msg)
                flash("Reset link sent to your email!", "success")
            else:
                flash("Email not found.", "danger")

        db.close()
    return render_template('forgot_password.html')

@resets.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=1800)
    except:
        flash("Invalid or expired link.", "danger")
        return redirect(url_for('forgot_password'))

    if request.method == 'POST':
        hashed_pw = generate_password_hash(request.form.get('password'))
        db = get_db()
        cursor = db.cursor()
        cursor.execute("UPDATE users SET password = %s WHERE email = %s", (hashed_pw, email))
        db.commit()
        db.close()
        flash("Password updated successfully!", "success")
        return redirect(url_for('forgot_password'))

    return render_template('reset_password.html')
