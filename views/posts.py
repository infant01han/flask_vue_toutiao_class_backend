# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 0004 14:39
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : posts.py
# @Software: PyCharm
from flask import request, jsonify

from app import app
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


@app.route('/api/get_posts')
@login_required
def get_posts(userid):
    pageIndex = int(request.args.get('pageIndex'))
    pageSize = int(request.args.get('pageSize'))

    try:
        userobj = User.objects(id=userid).first()
    except:
        return jsonify({'message':'user not found'})

    # posts = Post.objects(user=userobj).order_by("-created").skip(pageSize*(pageIndex-1)).limit(pageSize)
    posts = Post.objects(user=userobj).order_by("-created")
    paged_posts = posts.skip(pageSize*(pageIndex-1)).limit(pageSize)

    # post_lst = []
    # for obj in posts:
    #     tmp = obj.to_public_json()
    #     post_lst.append(tmp)

    # return jsonify({'data':post_lst})
    post_lst = paged_posts.to_public_jsons()

    return jsonify({'data':post_lst,'total': posts.count()})