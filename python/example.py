# -*- coding: utf-8 -*-
from replice_api import RepliceClient
import logging

KAKAO_BOT_HOST = "localhost"
KAKAO_BOT_PORT = 8080
LOGIN_ID = "testtest"
AUTH_KEY = "testtest"

logging.basicConfig(level = 1, format='%(asctime)s %(levelname)-10s %(message)s', datefmt='%m-%d %H:%M:%S')

r = RepliceClient(KAKAO_BOT_HOST, KAKAO_BOT_PORT, LOGIN_ID, AUTH_KEY)

def handle_message(replice, user_key, room_key, msg_id, message, country_iso, attachment = None):
  replice.send_message(user_key, room_key, msg_id, message)

def handle_add(replice, user_key, room_key, msg_id, country_iso):
  replice.send_message(user_key, room_key, msg_id, 'hi')

def handle_block(replice, user_key, room_key, msg_id):
  pass

def handle_result(replice, code, msg, msg_id):
  if code is not 200:
    logging.error(u'error %s(%d), msg_id(%d)'%(msg, code, msg_id))

r.on(u'request', handle_message)
r.on(u'result', handle_result)
r.on(u'add', handle_add)
r.on(u'block', handle_block)

while True:
  r.start()
  r.join()
  r.sleep(5)
