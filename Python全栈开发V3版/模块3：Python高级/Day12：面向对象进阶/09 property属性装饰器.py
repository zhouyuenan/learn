# (1) property属性装饰器
# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         # 私有化: __score
#         # 外部代码不能随意修改对象内部的状态
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
# yuan = Student("yuan", 88)
# 版本1
# alvin = Student("alvin", 66)
# print(yuan.get_score())
# yuan.set_score(99)
# print(yuan.score)


# 版本2
# from loguru import logger
# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         # 私有化: __score
#         # 外部代码不能随意修改对象内部的状态
#         self.__score = score
#
#     # 开放的一个查询成绩的接口
#     @property
#     def score(self):
#         logger.info(f"{self.name}查询了成绩{self.__score}")
#         return self.__score
#
#     @score.setter
#     def score(self, score):
#         if isinstance(score, int) and 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError("类型不一致错误")
#
#
# yuan = Student("yuan", 88)
# print(yuan.score)
# print(yuan.score)
# # yuan.set_score(100)
# yuan.score = 100
# print(yuan.score)
# print(yuan.score)
# (2) property属性函数
class Student(object):

    def __init__(self, name, score):
        self.name = name
        # 私有化: __score
        # 外部代码不能随意修改对象内部的状态
        self.__score = score

    # 开放的一个查询成绩的接口
    def __get_score(self):
        return self.__score

    def __set_score(self, score):
        if isinstance(score, int) and 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("类型不一致错误")

    score = property(__get_score, __set_score)

yuan = Student("yuan", 88)
print(yuan.score)
yuan.score = 100
print(yuan.score)
