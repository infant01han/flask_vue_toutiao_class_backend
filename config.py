# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 0003 11:27
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : config.py
# @Software: PyCharm
import os

flask_secret_key = "CHANGEME"

base = os.path.dirname(os.path.abspath(__file__))
image_upload_folder = os.path.join(base, 'images')