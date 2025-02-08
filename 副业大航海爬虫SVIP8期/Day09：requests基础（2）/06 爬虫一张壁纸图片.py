import requests

URL = "http://n.sinaimg.cn/sinacn14/30/w1080h1350/20180709/2bff-hezpzwu0436010.jpg"
Access_Headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
}

res = requests.get(url=URL, headers=Access_Headers)
# print(res.text)  # 响应数据必须得是一个文本[html/json]
print(res.content)  # 响应元数据, 字节流
with open("./test.jpg", mode="wb") as f:
    f.write(res.content)


