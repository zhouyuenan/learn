class Car(object):
    # 类属性
    total_cars = 0
    def __init__(self, make, model):
        self.make = make
        self.model = model
        print(f"self.__class__: {self.__class__}", id(self.__class__))
        self.__class__.total_cars += 1

    # 实例方法
    def accelerate(self):
        print(f"一辆{self.make}的{self.model}正在加速")

    @classmethod
    def show_total_cars(cls):
        print(id(cls))
        print(f"当前的total_cars: {cls.total_cars}")


class Cal(object):
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def mul(x, y):
        return x * y

# 实例对象调用
c = Cal()
c.add(1, 2)
print(c.add(10, 20))

# 类对象调用
Cal.add(10, 20)
print(Cal.add(10, 20))