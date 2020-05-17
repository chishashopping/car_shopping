import hashlib
from time import time

import requests
from rest_framework.utils import json


def send_sms(mobile):
    url = 'https://api.netease.im/sms/sendcode.action'
    data = {
        'mobile':mobile,  #你的手机号码
    }
    AppSecret = 'b3f682082454'
    AppKey = '48b443576010a1f56db456e941710331'
    #json类型
    Nonce = 'qweqdqwd12e01029i0dw0qwd'  #这个字符串时随机的长度不大于128，随便设
    CurTime = str(int((time() * 1000)))  #采用时间戳
    content =AppSecret + Nonce + CurTime
    CheckSum = hashlib.sha1(content.encode()).hexdigest()  #对上述进行按要求哈希
    headers = {   #设置请求头
        'AppKey':AppKey,
        'Nonce':Nonce,
        'CurTime':CurTime,
        'CheckSum':CheckSum
    }

    response = requests.post(url, data=data, headers=headers)#发送post请求
    str_result = response.text
    json_result = json.loads(str_result)

    return json_result