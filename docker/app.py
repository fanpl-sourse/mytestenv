# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 09:37
# @Author  : 饭盆里
# @File    : app.py
# @Software: PyCharm
# @desc    :
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'H' \
           'ello World! 该页面已被访问 {} 次。\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

# import time
# import redis
# from flask import Flask
#
# app = Flask(__name__)
# cache = redis.Redis(host='redis',port=6379)
#
# def get_hit_count():
#     retries = 5
#     while True:
#         try:
#             return cache.incr('hits')
#         except redis.exceptions.ConnectionError as exc:
#             if retries == 0:
#                 raise  exc
#             retries -= 1
#             time.sleep(0.5)
#
# @app.route('/')
# def hello():
#     count = get_hit_count()
#     return f'hello fanpl,I have been seen {count}times.'
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True)