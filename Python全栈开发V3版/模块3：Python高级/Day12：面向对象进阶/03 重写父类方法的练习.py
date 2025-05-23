# 案例1
class Animal(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def eat():
        print("eating...")

    @staticmethod
    def sleep():
        print("sleeping...")


class Dog(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    @staticmethod
    def swim():
        print("swimming...")


class Cat(Animal):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    @staticmethod
    def climb():
        print("climbing...")


class Bird(Animal):

    @staticmethod
    def fly():
        print("flying...")


alex = Dog("alex", 34, "斗牛犬")
alex.swim()
c1 = Cat("喵喵", 2, "white")
c1.climb()


# 案例2
class Base(object):

    def __init__(self):
        self.func(self)

    @staticmethod
    def func(self):
        print("in base")


class Son(Base):

    @staticmethod
    def func(self):
        print("in son")


s = Son()