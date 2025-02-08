import requests

cookies = {
    'xq_a_token': 'cccb558956c11f5aaf8b9a30bcf1f214117e8d67',
    'xqat': 'cccb558956c11f5aaf8b9a30bcf1f214117e8d67',
    'xq_r_token': '4e5ca4e31de699c97d46d00138f4460861fd1778',
    'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTczNjk4ODkwMCwiY3RtIjoxNzM1NDYwMzU4NzM0LCJjaWQiOiJkOWQwbjRBWnVwIn0.cPr-SiY8Rmufbz2E_wyc5t36IzDtPakkVOnoq1EBIwDRiGGFWgtQEiv5H75m0uqg5PkVSo5MzePQS9DVdrjXRtKg_3lbkTqYFLamQkzGSU4sGdrxn6oUSN_mHsoCjRycnbNsARJ5lHbDfv_oVNNAbrc6tqlvLRIJXSo5WYeYogYPbDVAkZjIgqa_jGFJ9W1gc1Gs3wthH89vi80IA0OUXC6lHeZXkn3ItwAXGw6J4syCazgPRFuoQDkcfeIdKCA8hI6XTI4OL3Ar7OE26hMA5iQXOfZd5RaHOI-k4qpthTItOosd87rSiK7G34YQaq8E1nmtXwejNfmY-u3Jleoyig',
    'cookiesu': '631735460396862',
    'u': '631735460396862',
    'device_id': '63b0c18d708635a1b1890f111366a6ec',
    'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1735460398',
    'HMACCOUNT': 'A5B201C8C00F69FA',
    'ssxmod_itna': 'eqmxBiD=eQuDcDGxBPxBbnbIq0=jveDk+zDRxWQhwqGNAoDZDiqAPGhDC8ft2G+ie4bzlApeKCz0iWdqfzZBidiI8Pg3dDHxY=DU27whoD435GwD0eG+DD4DWDmmHDnxAQDjxGp9uXwV=Dm4GW8qGfDDoDYf6uDitD4qDBIhdDKqGgGd4D0d+Nw0eDe3hx3WrUCntdEwxP57G9D0tQxBL5f=+9mnFCwGNP1P9xkgQDzu7DtqNMSudd6DtVRk03bAPPIDA2Q8D5Q0me+GEa77e57Y4qDs4n=ExrKB5FA7D6xD33fHD===',
    'ssxmod_itna2': 'eqmxBiD=eQuDcDGxBPxBbnbIq0=jveDk+zDRxWQhqA=9YD/7xKdK7=D2+eD=',
    'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1735460594',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': 'xq_a_token=cccb558956c11f5aaf8b9a30bcf1f214117e8d67; xqat=cccb558956c11f5aaf8b9a30bcf1f214117e8d67; xq_r_token=4e5ca4e31de699c97d46d00138f4460861fd1778; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTczNjk4ODkwMCwiY3RtIjoxNzM1NDYwMzU4NzM0LCJjaWQiOiJkOWQwbjRBWnVwIn0.cPr-SiY8Rmufbz2E_wyc5t36IzDtPakkVOnoq1EBIwDRiGGFWgtQEiv5H75m0uqg5PkVSo5MzePQS9DVdrjXRtKg_3lbkTqYFLamQkzGSU4sGdrxn6oUSN_mHsoCjRycnbNsARJ5lHbDfv_oVNNAbrc6tqlvLRIJXSo5WYeYogYPbDVAkZjIgqa_jGFJ9W1gc1Gs3wthH89vi80IA0OUXC6lHeZXkn3ItwAXGw6J4syCazgPRFuoQDkcfeIdKCA8hI6XTI4OL3Ar7OE26hMA5iQXOfZd5RaHOI-k4qpthTItOosd87rSiK7G34YQaq8E1nmtXwejNfmY-u3Jleoyig; cookiesu=631735460396862; u=631735460396862; device_id=63b0c18d708635a1b1890f111366a6ec; Hm_lvt_1db88642e346389874251b5a1eded6e3=1735460398; HMACCOUNT=A5B201C8C00F69FA; ssxmod_itna=eqmxBiD=eQuDcDGxBPxBbnbIq0=jveDk+zDRxWQhwqGNAoDZDiqAPGhDC8ft2G+ie4bzlApeKCz0iWdqfzZBidiI8Pg3dDHxY=DU27whoD435GwD0eG+DD4DWDmmHDnxAQDjxGp9uXwV=Dm4GW8qGfDDoDYf6uDitD4qDBIhdDKqGgGd4D0d+Nw0eDe3hx3WrUCntdEwxP57G9D0tQxBL5f=+9mnFCwGNP1P9xkgQDzu7DtqNMSudd6DtVRk03bAPPIDA2Q8D5Q0me+GEa77e57Y4qDs4n=ExrKB5FA7D6xD33fHD===; ssxmod_itna2=eqmxBiD=eQuDcDGxBPxBbnbIq0=jveDk+zDRxWQhqA=9YD/7xKdK7=D2+eD=; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1735460594',
    'origin': 'https://xueqiu.com',
    'priority': 'u=1, i',
    'referer': 'https://xueqiu.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
}

params = {
    'page': '1',
    'size': '9',
    '_type': '10',
    'type': '10',
    'md5__1632': 'euitiKDKSG8GODlp+q0=XKGKG=EFh9xDt=a4D',
}

response = requests.get('https://stock.xueqiu.com/v5/stock/hot_stock/list.json', params=params, cookies=cookies, headers=headers)
print(response.cookies)