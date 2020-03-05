# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 0003 9:25
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : jwtdemo.py
# @Software: PyCharm
import jwt
import datetime
from jwt import exceptions

SALT = 'apple'

def create_token():
    # 构造header
    headers = {
    'typ': 'jwt',
    'alg': 'HS256'
    }
    # 构造payload
    payload = {
    'user_id': 1, # 自定义用户ID
    'username': 'pig',
    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5)
    }
    result = jwt.encode(payload=payload, key=SALT, algorithm='HS256', headers=headers).decode('utf8')
    return result

def parse_payload(token):
    result = {'status': False, 'data': None, 'error': None}
    try:
        verified_payload = jwt.decode(token, SALT, True)
        result['status'] = True
        result['data'] = verified_payload
    except exceptions.ExpiredSignatureError:
            result['error'] = 'token已失效'
    except jwt.DecodeError:
            result['error'] = 'token认证失败'
    except jwt.InvalidTokenError:
            result['error'] = '非法的token'
    return result
if __name__ == '__main__':
    token = create_token()
    print(token)
    result = parse_payload(token)
    print(result)