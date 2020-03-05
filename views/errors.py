# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 0003 14:47
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : errors.py
# @Software: PyCharm
from flask import jsonify

from app import app


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        "message": "API endpoint not found"
    }), 404


@app.errorhandler(500)
@app.errorhandler(405)
def internal_server_error(e):
    return jsonify({
        "message": "Internal server error"
    }), 500


@app.errorhandler(413)
def request_entity_too_large(e):
    return jsonify({
        "message": "To large (max. 1 MB)"
    }), 413
