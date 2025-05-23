# print(len(100))
# print(len([1, 2, 3]))
# print(len({"a": "apple"}))
# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# l3 = l2
# print(l1 == l2)  # 值判断
# print(l1 is l2)  # 是否一样
# print(l2 is l3)  # 是否一样
#
#
# 缓存的容器类型
class Cache(object):

    def __init__(self):
        self.__data = []

    def add(self, item):
        # if 环境判断或者数据判断
        self.__data.append(item)

    def remove(self, item):
        self.__data.remove(item)

    def show(self):
        return self.__data

    def __len__(self):
        return len(self.__data)


cache = Cache()
cache.add("yuan")
cache.add("rain")
cache.add("alvin")
print(cache.show())
cache.remove("yuan")
print(cache.show())
print(len(cache))


# data = []
# data.append("yuan")
# data.append("rain")
# data.append("alvin")
# data.remove("alvin")
# print(data)