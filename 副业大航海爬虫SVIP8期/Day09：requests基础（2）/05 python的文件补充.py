# 打开或者创建一个文件

# (1) 补充一个追加模式
# wb和w
# ab和a (append)

# w: 覆盖写
# a: 追加写
f = open(file="./test1.txt", mode="a", encoding="utf-8")
f.write("apple")
f.write("banana")

# (2) close和with语句
f = open(file="./test1.txt", mode="r")
print(f.read())
f.close()

# (3) 上下文管理工具: with语句
with open(file="./test1.txt", mode="r") as f:
    print(f.read())
