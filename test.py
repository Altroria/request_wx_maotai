import requests

headers = {
'Host': 'web.sjhgo.com',
'accept': '*/*',
'content-type': 'application/json;charset=utf-8',
'accept-language': 'zh-cn',
'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c27) NetType/WIFI Language/zh_CN',
'referer': 'https://servicewechat.com/wxf91dc1d667af01f4/4/page-frame.html',
}

params = (
    ('method', 'pshop.work.exchangeGift.queryMessage'),
    ('token', 'e41f121c-6c81-4efe-b25c-125f803a6293'),
    ('sign', 'ea5fcfd32f9872a2b81fbcb1a09022a0'),
    ('app_key', '1570710699900928100_hgo1'),
)

data = '{"event_id":"166400004313156892","gbid":"Z77"}'

params1 = (
    ('method', 'pshop.work.exchangeGift.queryMessage'),
    ('token', '5975985e-c809-4593-9cb5-e5ae703f6c8c'),
    ('sign', '08906115c0e0df000594abe4442b91c2'),
    ('app_key', '1570710699900928100_hgo1'),
)

data1 = '{"event_id":"166400004313156892","gbid":"Z77"}'

response = requests.post(
    'https://web.sjhgo.com/omp-pshop-webin/rest',
    headers=headers,
    params=params1,
    data=data,
    verify=False)

print(response.text)