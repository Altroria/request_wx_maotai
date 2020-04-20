#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
import requests
import json
import time
import os
import datetime
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler



def searchCE():
    loctime= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    url='https://meal.spdbccc.toptastewin.com/chongzhi/api/goods/product?id=&pid=68'
    headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
    content = requests.get(url,  headers = headers)
    soup = BeautifulSoup(content.text, 'html.parser') 
    title = soup.find_all(class_ = 'product-title one-line')
    number =soup.find_all(class_ = 'one-line f-s-14 f-c-ad')
    for t in title:
        tit= t.get_text()
    for n in number:
        num = n.get_text()

    address1 = num.split(': ')  
    address2 = address1[1].split('份')
    stock =int(address2[0])
    printtxt=loctime+'\n商品名称：'+str(tit) +'\n库存:'+str(stock)
    print(printtxt)
    result2txt=str(printtxt)          
    with open('/root/py/pufaali.txt','a') as file_handle:   
        file_handle.write(result2txt)    
        file_handle.write('\n')   
        file_handle.close()     
    if stock > 10:
        login("SERVERID=0edeb5ac537378f418ec4e00f20ddc87|","PHPSESSID=3cbiauv8k1gp0fvhts8136ma37")
        textding=loctime+'\n商品名称：'+str(tit) +'\n库存：'+str(stock)
        # 安吉拉
        urldingA='https://oapi.dingtalk.com/robot/send?access_token=7ade068c85728b15c343f3b6285c1ff2c937ae6641142dd669abbcdfa0975eee'
        urlding = 'https://oapi.dingtalk.com/robot/send?access_token=293c1c15db0a85d9c8f748ec05f33edfe8bc534578a15fcb415d9fbcca9eb54d'
        pagrem22 = {
                                     "msgtype": "text",
                                     "text": {
                                     "content": textding}}
        headersding = {
                                     'Content-Type': 'application/json'}
        requests.post(urlding, data=json.dumps(pagrem22), headers=headersding)
        requests.post(urldingA, data=json.dumps(pagrem22), headers=headersding)




if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(searchCE, 'cron', hour='6-23', second='*/1')
    scheduler.start()