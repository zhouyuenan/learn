# (1) `__new__()`方法
"""
1. 开辟独立空间
2. __init__()执行
3. 返回该空间地址
"""


class Person(object):

    # 其中, cls参数表示类本身, *args和**kwargs参数用于接收传递给
    def __new__(cls, *args, **kwargs):
        print("__new__方法执行")
        return super().__new__(cls)
        # return object.__new__(cls)

    def __init__(self, name, age):
        print("__init__方法执行")
        self.name = name
        self.age = age


yuan = Person("yuan", 23)
print(yuan)
print(yuan.name)
print(yuan.age)


# __new__()方法应用
# 版本1
# class Config(object):
#
#     def __init__(self):
#         print("__init__已执行")
#
#
# c1 = Config()
# c2 = Config()
# print(id(c1))
# print(id(c2))


# 版本2
class Config(object):
    instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        print("__init__已执行")


c1 = Config()
c2 = Config()
print(id(c1))
print(id(c2))
