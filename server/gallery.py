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

gallery = Blueprint('gallery', __name__)

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

@gallery.before_request
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

@gallery.route('/gallery')
def gallery():
    user_id = session.get('user_id')
    sort = request.args.get('sort', 'new') 
    page = request.args.get('page', 1, type=int)
    per_page = 20
    offset = (page - 1) * per_page
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    current_user_id = g.user['id'] if g.user else None

    db = get_db()
    cursor = db.cursor(dictionary=True)

    query = """
        SELECT p.*, u.username, 
        (SELECT SUM(vote) FROM interactions WHERE target_id=p.id AND target_type='post') as score,
        (SELECT vote FROM interactions WHERE target_id=p.id AND target_type='post' AND user_id=%s) as user_vote
        FROM gallery_posts p 
        JOIN users u ON p.user_id = u.id 
        WHERE p.is_reported=0 
    """

    if sort == 'top':
        query += " ORDER BY score DESC"
    elif sort == 'random':
        query += " ORDER BY RAND()"
    else:
        query += " ORDER BY p.created_at DESC" 

    query += " LIMIT %s OFFSET %s"
    
    cursor.execute(query, (current_user_id, per_page, offset))
    posts = cursor.fetchall()
    
    cursor.close()
    db.close()
    
    return render_template('gallery.html', posts=posts, sort=sort, page=page)

@gallery.route('/galleryprofile/<int:uid>')
def gallery_profile(uid):
    db = get_db(); cursor = db.cursor(dictionary=True); me = session.get('user_id')
    
    cursor.execute("SELECT id, username, profile_pic FROM users WHERE id=%s", (uid,))
    user = cursor.fetchone()
    
    cursor.execute("SELECT * FROM gallery_posts WHERE user_id=%s AND is_reported=0", (uid,))
    posts = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) as f FROM social_relations WHERE followed_id=%s", (uid,))
    followers = cursor.fetchone()['f']

    cursor.execute("SELECT id FROM social_relations WHERE follower_id=%s AND followed_id=%s", (me, uid))
    is_following = cursor.fetchone()
    cursor.execute("SELECT id FROM social_relations WHERE follower_id=%s AND followed_id=%s", (uid, me))
    is_friend = bool(is_following and cursor.fetchone())

    cursor.execute("""
        SELECT u.id, u.username FROM users u
        JOIN social_relations r1 ON u.id = r1.followed_id
        JOIN social_relations r2 ON u.id = r2.follower_id
        WHERE r1.follower_id = %s AND r2.followed_id = %s
    """, (uid, uid))
    friends = cursor.fetchall()

    cursor.close(); db.close()
    return render_template('gallery_profile.html', user=user, posts=posts, followers=followers, 
                           is_following=bool(is_following), is_friend=is_friend, friends=friends, uid=uid)

@gallery.route('/api/gallery/upload', methods=['POST'])
def upload():
    if 'image' not in request.files: return redirect('/gallery')
    file = request.files['image']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['GALLERY_VAULT'], filename))
    
    db = get_db(); cursor = db.cursor()
    sql = """INSERT INTO gallery_posts (user_id, image_path, spot_name, species, lure_used, season, time_of_day) 
             VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql, (session.get('user_id'), f"gallery_vault/{filename}", 
                         request.form.get('spot'), request.form.get('species'), 
                         request.form.get('lure'), request.form.get('season'), request.form.get('time')))
    db.commit(); cursor.close(); db.close()
    return redirect(url_for('gallery'))

@gallery.route('/api/gallery/delete/<int:pid>', methods=['POST'])
def delete_post(pid):
    db = get_db(); cursor = db.cursor()
    cursor.execute("DELETE FROM gallery_posts WHERE id=%s AND user_id=%s", (pid, session.get('user_id')))
    db.commit(); cursor.close(); db.close()
    return jsonify({"status":"ok"})

@gallery.route('/api/comments/<int:post_id>')
def get_comments(post_id):
    db = get_db(); cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT c.*, u.username FROM comments c JOIN users u ON c.user_id=u.id WHERE post_id=%s AND is_reported=0", (post_id,))
    raw = cursor.fetchall(); nodes = {c['id']: {**c, 'replies': []} for c in raw}; tree = []
    for cid, c in nodes.items():
        if c['parent_id']:
            parent = nodes.get(c['parent_id']); 
            if parent: parent['replies'].append(c)
        else: tree.append(c)
    cursor.close(); db.close()
    return json.dumps(tree, cls=PyRBSocialEncoder)

@gallery.route('/api/post_comment', methods=['POST'])
def post_comment():
    d = request.json; db = get_db(); cursor = db.cursor()
    cursor.execute("INSERT INTO comments (post_id, user_id, parent_id, content) VALUES (%s,%s,%s,%s)", 
                   (d['post_id'], session.get('user_id'), d.get('parent_id'), d['content']))
    db.commit(); cursor.close(); db.close()
    return jsonify({"status":"ok"})

@gallery.route('/api/vote', methods=['POST'])
def vote():
    d = request.json; db = get_db(); cursor = db.cursor()
    sql = "INSERT INTO interactions (user_id, target_id, target_type, vote) VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE vote=%s"
    cursor.execute(sql, (session['user_id'], d['id'], d['type'], d['vote'], d['vote']))
    db.commit(); cursor.close(); db.close()
    return jsonify({"status":"ok"})

@gallery.route('/api/social/follow/<int:uid>', methods=['POST'])
def follow(uid):
    db = get_db(); cursor = db.cursor(); me = session.get('user_id')
    cursor.execute("SELECT id FROM social_relations WHERE follower_id=%s AND followed_id=%s", (me, uid))
    if cursor.fetchone():
        cursor.execute("DELETE FROM social_relations WHERE follower_id=%s AND followed_id=%s", (me, uid))
    else:
        cursor.execute("INSERT INTO social_relations (follower_id, followed_id) VALUES (%s, %s)", (me, uid))
    db.commit(); cursor.close(); db.close()
    return jsonify({"status":"ok"})
