# 打开或者创建一个文件
# 读模式: r: 读字符和rb: 读字节
# f: 操作文件的文件句柄

# (1) 读所有
# f = open("test.txt", mode="r", encoding="utf-8")
# data = f.read()  # 慎用
# print(data)

# (2) 读指定长度
# f = open("test.txt", mode="r", encoding="utf-8")
# data = f.read(2)  # 读一个字符
# print(data)

# (3) 循环遍历
f = open("test.txt", mode="r", encoding="utf-8")
for line in f:
    print(line, end="")
