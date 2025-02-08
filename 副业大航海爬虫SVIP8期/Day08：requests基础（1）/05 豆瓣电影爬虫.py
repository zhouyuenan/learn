import json

import requests
tags = input("电影类型:")

folk_headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "referer": "https://movie.douban.com/explore"
}
folk_params = {
    "start": 0,
    "count": 60,
    "tags": tags
}
target_url = "https://m.douban.com/rexxar/api/v2/movie/recommend"
res = requests.get(headers=folk_headers, url=target_url, params=folk_params)
print(res.text) # 响应体是一个页面，就没有办法用Json转换
print(res.json()) # 响应体是Json字符串，res.json()就会将爬虫得到的json字符串反序列化
print(json.loads(res.text).get("count"))