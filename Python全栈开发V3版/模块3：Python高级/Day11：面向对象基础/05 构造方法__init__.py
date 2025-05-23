# 声明类
class Dog:
    # 类属性
    legs_num = 4
    has_hair = True
    has_tail = True
    # 类方法

    def __init__(self, name, breed, color, age, weight):
        print("__init__构造方法执行")
        print("self:::" ,id(self))
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
        self.weight = weight

    def init_prepare(self, name, breed, color, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age

    def bark(self):
        print("self:::", self)
        print(f"{self.name}正在狂吠")

    def bite(self, person):
        print(f"{self.name}咬{person}")

    def fetch(self):
        print(f"{self.name}狗捡球")

    def show_info(self):
        print(f"名字: {self.name}, 品种: {self.breed}, 颜色: {self.color}, 年龄: {self.age}, 体重: {self.weight}")

# 版本1
# alex = Dog()
# peiQi = Dog()
# # (1) self
# # print("alex:::", alex)
# # alex.bark()
# # peiQi.bark()
# # alex.bite("yuan")
# # alex.bite("rain")
# # (2)
# alex.init_prepare("李杰", "斗牛犬", "浅灰色", 5)
# # alex.name = "李杰"
# # alex.breed = "斗牛犬"
# # alex.color = "浅灰色"
# # print(alex.name)
# # alex.age = 10
# alex.bark()
# # # alex.bite("yuan")
# alex.show_info()
# peiQi.init_prepare("武大郎", "斗牛犬", "浅灰色", 10)
# # peiQi.name = "武大郎"
# # peiQi.breed = "斗牛犬"
# # peiQi.color = "浅灰色"
# # peiQi.age = 5
# peiQi.bark()
# peiQi.show_info()
# 版本2
"""
类实例化步骤
(1) 开辟实例空间
(2) 调用__init__(实例空间地址)
(3) 将实例空间地址作为类的实例化的返回值
"""
alex = Dog("李杰", "斗牛犬", "浅灰色", 5, 60)
print("alex:::" ,id(alex))
alex.show_info()
peiQi = Dog("武大郎", "斗牛犬", "浅灰色", 10, 70)
print("peiQi:::" ,id(peiQi))