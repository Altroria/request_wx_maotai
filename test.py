# -*- coding: utf-8 -*-
import requests
import json
import time
import os
file_path = os.path.join(os.getcwd() + "/user.json")
from apscheduler.schedulers.blocking import BlockingScheduler


def get_token():
    with open(file_path) as f:
        data = json.load(f)
        f.close
        for cookie in data:
            a = ({'token': cookie['token'], "sign": cookie['sign']})
        return (a)


def wx_maotai():

    headers = {
        'Host':
        'web.sjhgo.com',
        'accept':
        '*/*',
        'content-type':
        'application/json;charset=utf-8',
        'accept-language':
        'zh-cn',
        'user-agent':
        'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c27) NetType/WIFI Language/zh_CN',
        'referer':
        'https://servicewechat.com/wxf91dc1d667af01f4/4/page-frame.html',
    }

    params = (
        ('method', 'pshop.work.exchangeGift.queryMessage'),
        ('token', get_token()["token"]),
        ('sign', get_token()["sign"]),
        ('app_key', '1570710699900928100_hgo1'),
    )

    data = '{"event_id":"166400004313156892","gbid":"Z77"}'

    response = requests.post(
        'https://web.sjhgo.com/omp-pshop-webin/rest',
        headers=headers,
        params=params,
        data=data,
        verify=False)
    print(response)


wx_maotai()