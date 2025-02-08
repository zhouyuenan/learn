import requests
Access_URL = "https://v3-microapp-dcar.dcarvod.com/a37a9a29d4203e7689707f1102eeae0a/676f7737/video/tos/cn/tos-cn-ve-4/owXAVAiEcSBFIXQdwW3xi94gfxmTazEAmRI5CM/?a=36&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&cd=0%7C0%7C0%7C0&cv=1&br=2637&bt=2637&cs=0&ds=4&eid=21760&ft=k7cKGVVyw3XRZ_8jmo~xj7ScoApPkfgZvrKE59XEmo0g3cI&mime_type=video_mp4&qs=0&rc=Nzs2O2kzOjw2NDg7Mzg7ZkBpanc6M2s5cnY8dDMzNDczM0BhNTYzXmIyXi8xNl9gLTRfYSNeL2ZfMmRzZHBgLS1kLWFzcw%3D%3D&btag=c0000e00038000&dy_q=1735354049&feature_id=df0cd2e352f757347f92c05051e140af&l=20241228104729FF4BAEB29FEED92BACB9"
Access_Headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
}
res = requests.get(url=Access_URL, headers=Access_Headers)
with open("./AMG.mp4", mode="wb") as f:
    f.write(res.content)
