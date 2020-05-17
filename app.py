# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 0003 0:29
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : app.py
# @Software: PyCharm
from flask import Flask, request
from flask_cors import CORS

import config
from model import Category

app = Flask(__name__)
app.config["SECRET_KEY"] = config.flask_secret_key
CORS(app)

from views.auth import *
from views.category import *
from views.errors import *
from views.posts import *
from views.upload import *
from views.user import *



if __name__ == '__main__':
    # Category(name='java').save()
    # Category(name='python').save()
    # Category(name='css').save()
    app.run()
