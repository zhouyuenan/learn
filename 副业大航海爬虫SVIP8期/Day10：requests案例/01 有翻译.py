import json

import requests
while 1:
    word = input("请输入翻译的单词：")
    Access_URL = "https://aidemo.youdao.com/trans"
    Access_Headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
        "referer": "https://ai.youdao.com/"
    }
    Access_Datas = {
        "q": word,
        "from": "auto",
        "to": "auto"
    }
    res = requests.post(url=Access_URL, params=Access_Datas)
    result = res.json().get("translation")[0]
    print(result)
    print(type(result))

