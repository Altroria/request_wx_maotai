# -*- coding: utf-8 -*-
import requests
import json
import time
import os
file_path = os.path.join(os.getcwd() + "/token.json")
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

    if json.loads(response.text)['data'] == '请求访问令牌非法,请重新登录':
        requests.get(
            'http://sc.ftqq.com/SCU93922T5afdfdbac6c06b06a0a413398a63c58e5e95901990f2d.send?text=token失效,重新登录'
        )
    elif json.loads(response.text)['data'] == '远程非法数据请求!':
        requests.get(
            'http://sc.ftqq.com/SCU94798Tf2c690b6bbdf8cbd685773714ac081a25e9e4f0cc853f.send?text=远程非法请求数据'
        )
    elif json.loads(response.text)['data'] == '服务繁忙，稍后再试':
        requests.get(
            'http://sc.ftqq.com/SCU94798Tf2c690b6bbdf8cbd685773714ac081a25e9e4f0cc853f.send?text=服务繁忙，稍后再试'
        )
        time.sleep(300)
    else:
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
                num = int(float(q["sl"]))
                if num >= 2:
                    aaa = "店名" + ":" + q[
                        "mktid_name"] + "\n\n" + "地址" + ":" + q[
                            "address"] + "\n\n" + "库存" + ":" + q["sl"] + "\n\n"
                    bbb = bbb + aaa
                    title = q["mktid_name"] + "\n\n"
                    requests.get(
                        'http://sc.ftqq.com/SCU94798Tf2c690b6bbdf8cbd685773714ac081a25e9e4f0cc853f.send?text='
                        + title + "补货了库存" + '&desp=' + str(bbb) + "'")

                    requests.get(
                        'http://sc.ftqq.com/SCU94093T40ff79741772f12c973146a6f8cbfe0b5e97af0555a10.send?text='
                        + title + '&desp=' + str(bbb) + "'")


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(wx_maotai, 'cron', hour='6-23', second='*/1')
    scheduler.start()
