s = str("Hello, World!!!")
print(s, type(s))
s.lower()
print(s.lower())

l = []
li = list((1, 2, 3))
li.append(4)
print(li)

d = dict({"k1": "v1"})

class Dog(object):
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


# (1) 任何一个实例对象都属于本身类型
alex = Dog("李杰", "斗牛犬", "浅灰色", 5, 60)
print(alex)
print(type(alex))
# (2) 自定义类型对象属于可变数据类型
alex.age = 10
print(alex.age)
# (3) 实例对象也是一等公民: 变量传递, 作为函数参数, 作为函数返回值
# 变量传递
x = alex
print(x.name)
print(x.age)
alex.age = 10000
print(x.age)

def foo(x):
    print(x)
    print(type(x))
    x.append(4)

# a = 1000
b = [1, 2, 3]
# foo(a)
foo(b)
print(b)

def bar(y):
    print(y, type(y))
    y.age = 10000
bar(alex)

def test():
    peiQi = Dog("武大郎", "斗牛犬", "浅灰色", 10, 70)
    return peiQi

pq = test()
print(pq.name)
print(pq.age)