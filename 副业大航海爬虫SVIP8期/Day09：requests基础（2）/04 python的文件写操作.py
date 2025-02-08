# 打开或者创建一个文件
# 读模式: w: 写字符和wb: 写字节
# f: 操作文件的文件句柄
# w: 写字符

# (1) 写字符
# f = open(file="满江红.txt", mode="w", encoding="utf-8")
# f.write("123\n")
# f.write("456")
# f.close()

# (2) 将test.txt中的内容写到满江红.txt, 结尾加上!
f_read = open(file="./test.txt", mode="r", encoding="utf-8")
f_write = open(file="./满江红.txt", mode="w", encoding="utf-8")
for line in f_read:
    data = line.replace("\n", "") + "!" + "\n"
    f_write.write(data)

# (3) 将image拷贝一份, 叫image2
f1 = open(file="./test2.jpg", mode="wb")
f2 = open(file="./test.jpg", mode="rb")
for i in f2:
    f1.write(i)
