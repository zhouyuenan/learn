# 重写父类方法
class Animal(object):

    @staticmethod
    def eat():
        print("eating...")

    @staticmethod
    def sleep():
        print("sleeping...")


class Dog(Animal):

    @staticmethod
    def swim():
        print("swimming...")

    # @staticmethod
    def sleep(self):
        print("sleeping...")


class Cat(Animal):

    @staticmethod
    def climb():
        print("climbing...")


class Fly(object):

    @staticmethod
    def fly():
        print("flying...")


class Eagle(Animal, Fly):
    pass


class Bat(Animal, Fly):
    pass


alex = Dog()
b1 = Bat()
b1.fly()
b1.sleep()
e1 = Eagle()
e1.fly()