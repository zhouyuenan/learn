import json

import requests

new_list = []
for i in range(1, 11):
    Access_Data = {
        "page": i
    }
    Access_Headers = {
        "referer": "https://www.icve.com.cn/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
    }
    Access_URL = "https://www.icve.com.cn/portal/portal/getSchoolList"

    response = requests.post(url=Access_URL, data=Access_Data, headers=Access_Headers)
    print(response.text)
    print(response.encoding)
    data = response.json()
    print(type(data))
    print(type(data["list"]))
    result = json.loads(data["list"])
    print(len(result))
    new_list.extend(result)
    # i = 0
    # for i in range(0, len(result)):
    #     print(result[i]["Name"])
with open("./school.json", mode="w") as f:
    f.write(json.dumps(new_list))