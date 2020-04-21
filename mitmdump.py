import re
import json
import os
file_path = os.path.join(os.getcwd() + "/token.json")

# 这个地方必须这么写 函数名：response


def response(flow):
    # 通过抓包软包软件获取请求的接口
    if 'https://web.sjhgo.com/omp-pshop-webin/rest' in flow.request.url:
        # 数据的解析
        token = flow.request.url.split('&')[1]
        sign = flow.request.url.split('&')[2]
        t_json = [{'token': token.split('=')[1], "sign": sign.split('=')[1]}]
        with open(file_path, 'a') as f:
            f.write(json.dumps(t_json))
