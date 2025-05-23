# 声明类
class Dog:
    # 类属性
    legs_num = 4
    has_hair = True
    has_tail = True
    # 类方法

    def bark(self):
        print("self:::", self)
        print(f"{self.name}正在狂吠")

    def bite(self, person):
        print(f"{self.name}咬{person}")

    def fetch(self):
        print(f"{self.name}狗捡球")

    def show_info(self):
        print(f"名字: {self.name}, 品种: {self.breed}, 颜色: {self.color}, 年龄: {self.age}")

alex = Dog()
# peiQi = Dog()
# (1) self
# print("alex:::", alex)
# alex.bark()
# peiQi.bark()
# alex.bite("yuan")
# alex.bite("rain")
# (2)
alex.name = "李杰"
alex.breed = "斗牛犬"
alex.color = "浅灰色"
print(alex.name)
alex.age = 10
alex.bark()
alex.bite("yuan")
alex.show_info()
# peiQi.bark()