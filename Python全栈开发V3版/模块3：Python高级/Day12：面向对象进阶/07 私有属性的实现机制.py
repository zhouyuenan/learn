# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         # 私有化: __score
#         self.__score = score
#
#     # 开放的一个查询成绩的接口
#     def get_score(self):
#         return self.__score
#
#     def set_score(self, score):
#         if isinstance(score, int) and 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError("类型不一致错误")
#
#
# alvin = Student("alvin", 66)
# yuan = Student("yuan", 88)
# print(yuan.__score)
# print(dir(yuan))
# print(yuan.__dict__)
# yuan.set_score(100)
# print(yuan.get_score())
# print(yuan._Student__score)
# yuan._Student__score = 10000
# print(yuan.get_score())


# 案例
class Person(object):

    def __init__(self, name, score):
        self.name = name
        self._score = score


class Student(Person):

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score


yuan = Student("yuan", 66)
print(yuan.__dict__)
print(yuan.get_score())
print(dir(yuan))