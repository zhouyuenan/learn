# (2) ·__str__()·方法
# class Person(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("__init__()方法执行")
#
#     def __str__(self):
#         print("__str__()方法执行")
#         # return "Hello, World!!!"
#         # return 100
#         # return self.name
#         return f"姓名: {self.name}, 年龄: {self.age}"
#
#
# yuan = Person("yuan", 23)
# print(yuan)
# # 触发__str__()执行的是str()
# str(yuan)
# alex = Person("alex", 33)
# print(alex)


# (3) `__eq__()`方法
# 案例1
# class Person(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("__init__()方法执行")
#
#     # 触发机制: ==
#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age
#         # return True
#
#
# yuan = Person("xxx", 23)
# alex = Person("xxx", 33)
# alex.__setattr__("age", 23)
# print(yuan == alex)
# print(alex == yuan)


# 案例2
class Dog(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("__init__()方法执行")

    def __eq__(self, other):
        print("Dog类的__eq__()方法")
        return self.age == other.age


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("__init__()方法执行")

    # 触发机制: ==
    def __eq__(self, other):
        print("Person类的__eq__()方法")
        return self.name == other.name and self.age == other.age
    # return True


yuan = Person("yuan", 23)
alex = Dog("alex", 23)
print(yuan == alex)
print(alex == yuan)