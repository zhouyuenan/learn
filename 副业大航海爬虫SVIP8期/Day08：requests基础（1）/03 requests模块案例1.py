import json

import requests

url = "https://www.python.org/search/?q=version&submit="
my_headers = {
    "content-type": "application/json"
}
my_params = {
    "a": "apple",
    "b": "banana"
}
my_data = {
    "name": "yuan",
    "pwd": "123"
}

# res = requests.get(url=url)
# res = requests.get(url=url, params=my_params)
# res = requests.post(url=url)
# res = requests.post(url=url, data=my_data)
# 发送Json数据数据方式1：有坑
# res = requests.post(url=url, json=my_data)
# 发送Json数据数据方式2：推荐
res = requests.post(url=url, data=json.dumps(my_data, separators=(",", ":")), headers=my_headers)
# res: 相应信息对象：相应状态码 响应头 响应体
# print(res.status_code)
# print(res.headers)
# print(res.text)
