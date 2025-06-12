# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import json

def send_message_to_jandi(message):
    # Python 2.7에서 모든 문자열이 자동으로 유니코드로 처리됨
    webhook_url ='https://wh.jandi.com/connect-api/webhook/24226711/8229d0b7efbe96a13ff3748c348bf6d4'
    headers = {'Content-Type': 'application/json'}
    

    
    
    payload = {
        "body": message,
        "connectColor": "#0000FF",
        "connectInfo": [
            {
                "title": "Maya Event",
                "description": "%s" % message
            }
        ]
    }

    json_payload = json.dumps(payload, ensure_ascii=False).encode('utf-8')

    response = requests.post(webhook_url, headers=headers, data=json_payload)
    
    if response.status_code == 200:
        print("메시지가 잔디로 성공적으로 전송되었습니다.")
    else:
        print("메시지 전송 실패: %s" % response.status_code)

# 유니코드 문자열 처리
send_message_to_jandi(u"이게왜되는거냐.")