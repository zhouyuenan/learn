# (1) 创建一个名为 `Circle` 的类，并为其添加计算面积（area）、周长（circumference）等方法。
import math


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius * self.radius, 2)

    def calculate_circumference(self):
        return round(2 * math.pi * self.radius, 2)


c1 = Circle(10)
c2 = Circle(20)
print(f"c1的周长是{c1.calculate_circumference()}, c1的面积是{c1.calculate_area()}")
print(f"c2的周长是{c2.calculate_circumference()}, c2的面积是{c2.calculate_area()}")


# (2) 人狗大战

class Person(object):

    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def kick_dag(self, dog):
        print(f"{self.name}踢了{dog.name}一下")
        # 狗掉血
        dog.decrease_health(10)

    def decrease_health(self, amount):
        self.health -= amount


class Dog(object):

    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def bite(self, person):
        print(f"{self.name}咬了{person.name}一下")
        # 人掉血20
        person.decrease_health(20)

    def decrease_health(self, amount):
        self.health -= amount


yuan = Person("yuan")
alex = Dog("alex")
alex.bite(yuan)
print(yuan.health)
yuan.kick_dag(alex)
print(alex.health)
yuan.kick_dag(alex)
yuan.kick_dag(alex)
print(alex.health)


# (3) 创建一个名为 `BankAccount` 的类
class BankAccount(object):

    def __init__(self, account_num, balance):
        self.account_num = account_num
        self.balance = balance

    def deposit(self, amount):
        print(f"{self.account_num}存款{amount}元!")
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.account_num}取款{amount}元, 当前余额: {self.balance}")
        else:
            print("提取金额大于余额!")

    def get_balance(self):
        # if判断
        return self.balance


account01 = BankAccount("123456", 10000)
account01.deposit(20000)
account01.withdraw(50000)
account01.withdraw(5000)


# (4) 书籍管理
class Book(object):
    book_list = []
    book_count = 0

    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

        Book.book_list.append(self)
        Book.book_count += 1

    @classmethod
    def show_books(cls):
        for book in cls.book_list:
            print(f"书籍名称: {book.title}, 作者: {book.author}, 出版年份: {book.publication_year}")


book1 = Book("西游记", "吴承恩", 1592)
book2 = Book("水浒传", "吴承恩", 1592)
book3 = Book("红楼梦", "吴承恩", 1592)
book4 = Book("三国演义", "吴承恩", 1592)

Book.show_books()
print(Book.book_count)
