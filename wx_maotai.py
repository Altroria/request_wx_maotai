# -*- coding: utf-8 -*-
import requests
import json
import time

while True:
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
        ('token', '8b150121-fce5-4321-bef5-d8d74b51df10'),
        ('sign', 'dee1e46310348bc64da5a093d2f0f706'),
        ('app_key', 'hgo'),
    )

    data = '{"event_id":"166400004313156892","gbid":"Z77"}'

    response = requests.post(
        'https://web.sjhgo.com/omp-pshop-webin/rest',
        headers=headers,
        params=params,
        data=data,
        verify=False)

    params1 = (
        ('method', 'pshop.work.exchangeGift.queryMessage'),
        ('token', '8b150121-fce5-4321-bef5-d8d74b51df10'),
        ('sign', 'd83fe15ac2ee2b74310fe40fba5fda05'),
        ('app_key', 'hgo'),
    )

    data1 = '{"event_id":"166273215184211208","gbid":"Z81"}'

    response1 = requests.post(
        'https://web.sjhgo.com/omp-pshop-webin/rest',
        headers=headers,
        params=params1,
        data=data1,
        verify=False)

    if json.loads(response.text)['data'] != '请求访问令牌非法,请重新登录':
        try:
            res = json.loads(response.text)['data']['mktList']
        except:
            res = None
            print("没有库存")

        if res != None and res != []:
            i = 0
            bbb = ""
            while i < len(res):
                q = res[i - 1]
                i = i + 1
                aaa = "店名" + ":" + q["mktid_name"] + "\n\n" + "地址" + ":" + q[
                    "address"] + "\n\n" + "库存" + ":" + q["sl"] + "\n\n"
                bbb = bbb + aaa
                title = q["mktid_name"] + "\n\n"

            requests.get(
                'http://sc.ftqq.com/SCU93922T5afdfdbac6c06b06a0a413398a63c58e5e95901990f2d.send?text=' + title + "补货了库存" + '&desp=' + str(bbb) + "'")
            requests.get(
                'http://sc.ftqq.com/SCU94093T40ff79741772f12c973146a6f8cbfe0b5e97af0555a10.send?text='
                + title + '&desp=' + str(bbb) + "'")
        time.sleep(10)
    else:
        requests.get(
            'http://sc.ftqq.com/SCU93922T5afdfdbac6c06b06a0a413398a63c58e5e95901990f2d.send?text=token失效,重新登录'
        )
        break
