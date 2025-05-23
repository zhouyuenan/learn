# (1) type()和isinstance()
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


alex = Dog()
print(type(alex))
print(isinstance(alex, Dog))
print(isinstance(alex, Animal))


# (2) dir()和__dict__
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    @staticmethod
    def test(self):
        pass


alex = Student("alex", 32)
print(alex.__dict__)
print(dir(alex))
print(alex.__class__)