# 缓存的容器类型
class Cache(object):

    def __init__(self):
        self.__data = {}

    def add(self, key, value):
        # if 环境判断或者数据判断
        self.__data[key] = value

    def remove(self, key):
        self.__data.pop(key)

    def show(self):
        return self.__data

    def __len__(self):
        return len(self.__data)


cache = Cache()
# 版本1
# cache.add("name", "yuan")
# cache.add("age", 18)
# print(cache.show())
# cache.remove("age")
# print(cache.show())
# print(len(cache))
print("test")
print("test")
print("test")
