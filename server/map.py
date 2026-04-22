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

map = Blueprint('map', __name__)

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

@map.before_request
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

@map.route('/map')
def show_map():
    return render_template('map.html')

@map.route('/api/pins', methods=['GET', 'POST'])
def handle_pins():
    user_id = session.get('user_id')
    print(f"--- DEBUG: User ID is {user_id} ---")

    if not user_id:
        return jsonify({"error": "Not logged in"}), 401

    db = get_db()
    cursor = db.cursor(dictionary=True)

    try:
        if request.method == 'POST':
            data = request.json
            sql = "INSERT INTO fishing_spots (user_id, lat, lng, location_name, species, season, time_of_day, lure_used) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (user_id, data['lat'], data['lng'], data['location_name'], data['species'], data['season'], data['time_of_day'], data['lure_used']))
            db.commit()
            return jsonify({"status": "success"})

        cursor.execute("SELECT *, DATE_FORMAT(created_at, '%%Y-%%m-%%d') as created_at FROM fishing_spots WHERE user_id = %s", (user_id,))
        pins = cursor.fetchall()
        for p in pins:
            p['lat'], p['lng'] = float(p['lat']), float(p['lng'])
        return jsonify(pins)

    except Exception as e:
        print(f"--- DATABASE ERROR: {e} ---")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        db.close()
        
@map.route('/api/deletepin/<int:pin_id>', methods=['DELETE'])
def delete_pin(pin_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM fishing_spots WHERE id = %s", (pin_id,))
    db.commit()
    cursor.close()
    db.close()
    return jsonify({"status": "deleted"})
