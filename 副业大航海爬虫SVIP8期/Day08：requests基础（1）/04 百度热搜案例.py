import requests
import re
# 四要素：请求方式、URL、请求头、载荷

# (1) 爬虫
my_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
url = "https://www.baidu.com/"
res = requests.get(headers=my_header, url=url)
# print(res.text)

# (2) 数据解析: re/xpath
ret = re.findall('<span class="title-content-title">(.*?)</span>', res.text)
print(ret)