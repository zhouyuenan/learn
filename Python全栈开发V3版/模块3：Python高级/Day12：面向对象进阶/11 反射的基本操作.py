class Person(object):

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


yuan = Person("yuan", 22, "male")
# 实例对象.属性变量
print(yuan.name)
yuan.age = 100
print(yuan.age)
# print(yuan.attribute)
while 1:
    # 方案1
    attribute = input("请输入您想查询的yuan的某个属性值: ")
    # if attribute == "name":
    #     print(yuan.name)
    # elif attribute == "age":
    #     print(yuan.age)
    # 反射
    print(getattr(yuan, "name"))  # yuan.name
    print(getattr(yuan, "age"))  # yuan.age
    if hasattr(yuan, attribute):
        val = getattr(yuan, attribute)
        print(f"yuan的{attribute}是{val}")
    else:
        print(f"yuan没有{attribute}的属性")
        choice = input("是否给yuan加入该属性[Y/N]")
        if choice == "Y":
            value = input(f"请输入yuan对象{attribute}属性值")
            setattr(yuan, attribute, value)
        else:
            pass