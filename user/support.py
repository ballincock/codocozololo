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

support = Blueprint('support', __name__)

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

@support.before_request
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

@support.route('/admin/panel')
def admin_panel():
    if session.get('user_id') != 1: return redirect('/')
    db = get_db(); cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT r.*, u.username FROM report_tickets r JOIN users u ON r.reporter_id=u.id WHERE status='pending'")
    tickets = cursor.fetchall(); cursor.close(); db.close()
    return render_template('admin.html', reports=tickets)

@support.route('/api/admin/resolve', methods=['POST'])
def resolve():
    if session.get('user_id') != 1: return "Forbidden", 403
    d = request.json; db = get_db(); cursor = db.cursor()
    if d['action'] == 'delete':
        tbl = "gallery_posts" if d['type'] == 'post' else "comments"
        cursor.execute(f"UPDATE {tbl} SET is_reported=1 WHERE id=%s", (d['target_id'],))
    cursor.execute("UPDATE report_tickets SET status='resolved' WHERE id=%s", (d['report_id'],))
    db.commit(); cursor.close(); db.close()
    return jsonify({"status":"ok"})
