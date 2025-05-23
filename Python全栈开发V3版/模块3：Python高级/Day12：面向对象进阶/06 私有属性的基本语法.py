class Student(object):

    def __init__(self, name, score):
        self.name = name
        # 私有化: __score
        self.__score = score

    # 开放的一个查询成绩的接口
    def get_score(self):
        return self.__score

    def set_score(self, score):
        if isinstance(score, int) and 0<=score<=100:
            self.__score = score
        else:
            raise ValueError("类型不一致错误")

alvin = Student("alvin", 66)
yuan = Student("yuan", 88)

# 案例1
# alvin.score = 100
# print(alvin.score)
# print(yuan.name)
# print(yuan.score)
# yuan.score = 100
# print(yuan.score)

# 案例2
# print(yuan.name)
# print(yuan.get_score())
# yuan.__score = 1000
# yuan.set_score(99)
# print(yuan.get_score())

# 案例3
class Student2(object):

    def __init__(self, name, score):
        self.name = name
        # 私有化: __score
        # 外部代码不能随意修改对象内部的状态
        self.score = score


rain = Student2("yuan", 88)
rain.score = "Hello, World!!!"

yuan.set_score("Hello, World!!!")