# class Animal(object):
#
#     @staticmethod
#     def eat():
#         print("eating...")
#
#     # @staticmethod
#     def sleep(self):
#         self.swim()
#         print("sleeping...")
#         print(f"self:::", id(self))
#
#
# class Dog(Animal):
#
#     @staticmethod
#     def swim():
#         print("swimming...")
#
#
# class Cat(Animal):
#
#     @staticmethod
#     def climb():
#         print("climbing...")
#
#
# class Bird(Animal):
#
#     @staticmethod
#     def fly():
#         print("flying...")


# 实例对象.变量 查询顺序 [实例空间 -> 类空间 -> 父类空间 -> ...]
# alex = Dog()
# print(id(alex))
# # alex.swim()
# # alex.eat()
# alex.sleep()
# c = Cat()
# c.sleep()

# 重写父类方法
class Animal(object):

    @staticmethod
    def eat():
        print("eating...")

    # @staticmethod
    def sleep(self):
        print(f"self:::", id(self))
        print("sleeping...")


class Dog(Animal):

    @staticmethod
    def swim():
        print("swimming...")

    # @staticmethod
    def sleep(self):
        # print("sleeping...")
        # 调用父类原方法
        # 方式1: 类对象.方法(self, 其他参数)
        Animal.sleep(self)
        # 方式2: super
        # super().sleep()
        print("侧翻睡")


class Cat(Animal):

    @staticmethod
    def climb():
        print("climbing...")


class Bird(Animal):

    @staticmethod
    def fly():
        print("flying...")


alex = Dog()
print(id(alex))
alex.sleep()
