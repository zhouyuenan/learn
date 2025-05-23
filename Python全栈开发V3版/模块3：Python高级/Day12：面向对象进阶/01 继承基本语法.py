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


class Cat(Animal):

    @staticmethod
    def climb():
        print("climbing...")


class Bird(Animal):

    @staticmethod
    def fly():
        print("flying...")


# 实例对象.变量 查询顺序 [实例空间 -> 类空间 -> 父类空间]
alex = Dog()
alex.swim()
alex.eat()
alex.sleep()