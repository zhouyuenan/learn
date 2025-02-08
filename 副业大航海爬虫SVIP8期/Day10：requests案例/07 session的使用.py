import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'https://xueqiu.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'cookiesu=631735460396862; device_id=63b0c18d708635a1b1890f111366a6ec; .thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=; smidV2=20241229161958494c4fb1f8c4fbbd32dab6e4f6b25270008dd269c37e82810; acw_tc=1a0c66d617389793327828284e00c3d4dd84c2115de62a7480151c14588188; xq_a_token=b1d767edc014ddf478005982ba9e053910dad8dc; xqat=b1d767edc014ddf478005982ba9e053910dad8dc; xq_r_token=4ac6dcb5a1bd823260eef986e5e529b07195748d; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTc0MDg3NzAzNywiY3RtIjoxNzM4OTc5MzIyMjY4LCJjaWQiOiJkOWQwbjRBWnVwIn0.nXmotpuTKTX-u0LusMjc_qbKTxUh4waMTTPVXGGeEF0VeJIgG3xJPe6UIq85pW3jx3EdSNNlw07VTQAWGuBjltwT3Hy6DHW10kWkRu6P7MsxjLqPZAV4ERfV530AU-cmnjKcMQrIArJgCObJhMyakQvcW4LIfsmSVKyZblqx3p0dfZbn3h6xPOW26IqbuQmMN0fT8J3dh4m5cyaCZfSiTZIGrdOLmwlM3LnuddD9xkuSEru79jiHYTITn_Od3EA0B_h2V-WECpjDUvy5n5bQhr563Yr8RYLg1sjOOB8fliOLNmqd0djEX6whHzFQHh8HrikUJGf1XdzGjxW_IHi6JA; u=631735460396862; Hm_lvt_1db88642e346389874251b5a1eded6e3=1738979334; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1738979334; HMACCOUNT=A5B201C8C00F69FA; ssxmod_itna=iqmxuiDtKWTRqGHeGdD7AmYYK0=IeGCS4=iDjor+2GqGX=IYDZDiqAPGhDC3SzYhpoFY004qKUQ93IhTUbC8DQK3Cc2b4HF9Ro4GLDmKDyieoreDx6q0rD74irDDxD3Db8QDSDWKD9D0+CB2HsnxGWDm+CDWPDYxDrR2KDRxi7DDH=hx07DQH1FDDzFifPhDGiqjh+NK9mM6OzKlBKkY5D9coDs2GUFYypM9LPx/Bjc+Adjx0kdq0OZ6vGw6oPc=AsYt2WeYhi3erbk70K+QGPtohxqC4gKmpYTQUqvi3Fz2WeFDDWqYhK1iDD==; ssxmod_itna2=iqmxuiDtKWTRqGHeGdD7AmYYK0=IeGCS4=iDjor+2DA696hW4D/bt5DF2YmoNzK=D6jovi4gYjEIi1=yO775wSQnrfrqM9QnOrTqdbe87wPO7hIPugt1b6rmKKWzjRy5u6t2a+yRUhFe7hPZiqxhGmitn9DkWY=d1bbzmuDr6rIViDbRC74krFqogq7KQgKGt5=FZTYmxfCrZfF=CB8SBgKTU9ErtOzLI8FMivIZFTrZbvihC++eCbXF0DH5gqrsp9+26qz+aL4qh=6FVAOR2lgea3z3eHaZ6dSMj=vKa/iyuzZh6KrROkTrYf8k2Gz/+senbB2rI25tfPD7j5OhTZIuPwqtGxjI3z2Yae=ILt8oKDGcDG7EE+o04nEwCh5hYblhK1Y=hiDD',
}
# 实例化一个session对象
session = requests.session()

# session: 自动管理cookie
request = session.get(url="https://xueqiu.com/", headers=headers)
print(request.text)