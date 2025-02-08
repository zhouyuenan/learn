print("Hello, Yuan")
name = "周月南"
# python的编码：字符串.encode()生成的对应的字节数据
# 编码
result = name.encode("utf-8")  # 默认是utf8
print(result, type(result))  # <class 'bytes'>

# 字节两个用处(流向): 磁盘存储和网络传输
# 解码: 字节对象.decode(解码方式)生成对应的字符串
print(result.decode("utf-8"))
