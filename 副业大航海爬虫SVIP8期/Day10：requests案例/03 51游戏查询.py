import requests

Access_Headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
}
Access_Params = {
    "q": "传奇"
}
Access_URL = "https://game.51.com/search/action/game/"

res = requests.get(url=Access_URL, params=Access_Params, headers=Access_Headers)
print(res.encoding)
with open("./games.html", mode="w", encoding="utf-8") as f:
    f.write(res.text)
