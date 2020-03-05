# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 0003 9:44
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : auth.py
# @Software: PyCharm
from functools import wraps

import jwt
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from model import User

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "Authorization" in request.headers:
            # Check whether token was sent
            authorization_header = request.headers["Authorization"]

            # Check whether token is valid
            try:
                token = authorization_header.split(" ")[1]
                user = jwt.decode(token, app.config["SECRET_KEY"])
            except:
                return jsonify({"message": "you are not logged in"}), 401

            return f(userid=user["userid"], *args, **kwargs)
        else:
            return jsonify({"message": "you are not logged in"}), 401
    return wrap

from app import app


@app.route('/api/register',methods=['POST'])
def register():
    if not request.json.get("username"):
        return jsonify({"message": "Username not specified"}),409
    if not request.json.get("email"):
        return jsonify({"message": "Email not specified"}),409
    if not request.json.get("password"):
        return jsonify({"message": "Password not specified"}),409

    if User.objects(username=request.json.get("username")):
        return jsonify({"message": "Username not available"}),409
    if User.objects(email=request.json.get("email")):
        return jsonify({"message": "There is already an account with your email address"}),409

        # Hash password with sha256
    hashed_password = generate_password_hash(request.json.get("password"))

    new_user = User(
        username=request.json.get("username"),
        email=request.json.get("email"),
        password=hashed_password,
        head_img='',
        gender=1,
        user_followed=[]
    ).save()

    return jsonify({"message":"register success"})


@app.route('/api/login',methods=['POST'])
def login():
    if not request.json.get("username"):
        return jsonify({"error": "Username not specified"}), 409
    if not request.json.get("password"):
        return jsonify({"error": "Password not specified"}), 409

    try:
        username = request.json.get("username")
        print(username)
        users = User.objects(username=username)
    except:
        print('error')

    user = users.first()

    if user == None:
        return jsonify({"error": "User not found"}), 403



    if not check_password_hash(user.password, request.json.get("password")):
        return jsonify({"error": "Invalid password"}), 401

    token = jwt.encode({
        "userid": str(user.id),
        "username": user.username,
        "email": user.email,
        "password": user.password,
        "created": str(user.created)
    }, app.config["SECRET_KEY"])

    return jsonify({
        # "success": True,
        "message": '登录成功',
        "data": {
            "user": user.to_public_json(),
            "token": token.decode("UTF-8"),
            # "email": user.email,
            # "password": user.password,
            # "created": str(user.created)
        },

    })