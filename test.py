import json
import os
file_path = os.path.join(os.getcwd() + "/user.json")

print(file_path)
url = 'https://web.sjhgo.com/omp-pshop-webin/rest?method=pshop.work.exchangeGift.queryMessage&token=a0991008-4c75-4c0e-a3e3-d5c683059bf2&sign=d905701f2cfa066c6d8ccfbdbb68b2d8&app_key=1570710699900928100_hgo1'

token = url.split('&')[1]
sign = url.split('&')[2]

t_json = [{
    'token': token.split('=')[1],
    "sign": sign.split('=')[1]
}]
with open(file_path, 'a') as f:
    f.write(json.dumps(t_json))



with open(file_path) as f:
    data = json.load(f)
    f.close
for cookie in data:
    a = ({
        'token': cookie['token'],
        "sign": cookie['sign']
    })
print(a["token"])
