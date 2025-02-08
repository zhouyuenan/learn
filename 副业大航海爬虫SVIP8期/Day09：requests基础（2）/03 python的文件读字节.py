# 打开或者创建一个文件
# 读模式: r: 读字符和rb: 读字节
# f: 操作文件的文件句柄

# (1) 读文本文件
# f = open("test.txt", mode="rb")
# data = f.read()  # 慎用
# print(data)
# print(data.decode("utf-8"))

# (2) 读image, 视频, 音频
# f = open("test.jpg", mode="rb")
# data = f.read()
# print(data)
