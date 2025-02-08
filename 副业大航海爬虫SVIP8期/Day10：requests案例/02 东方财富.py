import requests
Access_URL = "https://www.eastmoney.com/"
Access_Headers = {
    "referer": "https://cn.bing.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
}
res = requests.get(url=Access_URL, headers=Access_Headers)
print(type(res.text))
print(res.content.decode("utf-8"))
with open("./dongfangcaifu.html", mode="w", encoding="utf-8") as f:
    f.write(res.content.decode("utf-8"))