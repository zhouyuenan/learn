import time

import requests
import json

cookies = {
    'acw_tc': '0aef832317353743090718658e00fa95909155f8cfcf3d2bbd2c73adb0557e',
    '_abfpc': '0b32821524d7fe384768e814ca0ac7711a322b91_2.0',
    'cna': 'e62ba30012515814398f977951a3ac50',
    'verifycode': 'F1BA8CA1E5E0BE806CC607D914780188@638710002482879965',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    # 'Cookie': 'acw_tc=0aef832317353743090718658e00fa95909155f8cfcf3d2bbd2c73adb0557e; _abfpc=0b32821524d7fe384768e814ca0ac7711a322b91_2.0; cna=e62ba30012515814398f977951a3ac50; verifycode=F1BA8CA1E5E0BE806CC607D914780188@638710002482879965',
    'Origin': 'https://www.icve.com.cn',
    'Referer': 'https://www.icve.com.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.post('https://www.icve.com.cn/portal/portal/getProjectInfoNew', cookies=cookies, headers=headers)
data = json.loads(response.json().get("list"))
print(type(data))

for i in range(0, len(data)):
    print(data[i])
    time.sleep(2)