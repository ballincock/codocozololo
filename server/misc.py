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

misc = Blueprint('misc', __name__)

@app.route('/ectoplasm')
def launch_ectoplasm():  
    if 'username' in session:
        name = session['username']
        token = hashlib.md5(f"{name}SECRET_SALT".encode()).hexdigest()
        return redirect(f"http://localhost:4567/ectoplasm/?name={name}&auth={token}")
    return redirect("http://localhost:4567/ectoplasm/")

@misc.route('/donate')
def admin_panel():
    return render_template('donate.html')

@misc.route('/weather')
def weather_widget():
    VC_API_KEY = 'YU87AQZC9FSKBEL8GL97CD6K3'
    city = "Wilmette"
    
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if user_ip not in ['127.0.0.1', 'localhost']:
        try:
            geo_data = requests.get(f"http://ip-api.com{user_ip}", timeout=5).json()
            if geo_data.get('status') == 'success':
                city = geo_data.get('city', city)
        except:
            pass

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={VC_API_KEY}&contentType=json"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            
            curr = data['currentConditions']
            weather_data = {
                'city': data['address'].capitalize(),
                'temp': round(curr['temp']),
                'desc': curr['conditions'],
                'icon': curr['icon'],
                'humidity': curr['humidity']
            }

            forecast_list = []
            for hour in data['days'][0]['hours'][:4]: 
                forecast_list.append({
                    'time': hour['datetime'][:5],
                    'temp': round(hour['temp']),
                    'icon': hour['icon']
                })
            
            bg_map = {'clear-day': 'clear-bg', 'cloudy': 'cloudy-bg', 'rain': 'rainy-bg'}
            bg_class = bg_map.get(curr['icon'], 'default-bg')

            return render_template('weather.html', 
                                   weather=weather_data, 
                                   forecast=forecast_list, 
                                   bg_class=bg_class)
        else:
            print(f"VC API Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Connection Error: {e}")

    return render_template('weather.html', weather=None)
