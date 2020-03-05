# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 0004 14:39
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : posts.py
# @Software: PyCharm
from flask import request

from app import app, jsonify
from model import User, Post
from views.auth import login_required


@app.route('/api/posts',methods=['POST'])
@login_required
def posts_create(userid):
    print(userid)
    user = User.objects(id=userid).first()

    coverLst = []
    for cover in request.json.get('cover'):
        coverLst.append(cover['id'])

    Post(
        title=request.json.get("title"),
        categories=request.json.get('categories'),
        content=request.json.get("content"),
        user=user,
        covers=coverLst,
        type=request.json.get('type'),
        comments=[],
        user_collect=[],
        user_agree=[],
    ).save()
    return jsonify({"message":"success"})
