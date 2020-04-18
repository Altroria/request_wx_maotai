# -*- coding: utf-8 -*-
import requests

headers = {
    'Host': 'web.sjhgo.com',
    'accept': '*/*',
    'content-type': 'application/json;charset=utf-8',
    'accept-language': 'zh-cn',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c27) NetType/WIFI Language/zh_CN',
    'referer': 'https://servicewechat.com/wxf91dc1d667af01f4/4/page-frame.html',
}

params1 = (
    ('method', 'efuture.omp.activities.buycoupon.submitorder'),
    ('token', 'e2e95920-8c39-453b-92b6-ae934781cf15'),
    ('sign', '4738161cd63cf153fbb53dcba67ede88'),
    ('app_key', 'hgo'),
)

params2 = (
    ('method', 'efuture.omp.activities.buycoupon.submitorder'),
    ('token', 'e2e95920-8c39-453b-92b6-ae934781cf15'),
    ('sign', '3cd7e2836baec6361b7f0961a97bc93f'),
    ('app_key', 'hgo'),
)



data = '{"channel_id":"WECHAT","event_id":"166273215184211208","cid":"0004538455","wxid":"oD-3T5IuXbzVwbGuUhh2HRvAFmEM","ctype":"05","isfl":"Y","name":"孙浩","mobile":"17621231905","exchage_mode":"1","mkt_name":"福州五四店","market":"6002","city":"3501","num":1,"points":20,"amount":0,"gh_state":"gh_4634ac035ced"}'




response = requests.post('https://web.sjhgo.com/omp-activity-webin/rest',
                         headers=headers, params=params2, data=data.encode('utf-8'), verify=False)
print(response.text)
