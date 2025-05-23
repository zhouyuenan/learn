# import cal, communication, mysql  # 不推荐
# import cal
# import cal
# import cal
# import communication
# import mysql


# (1) 模块作为一等公民
# x = cal
# x.add(2, 5)
#
# def ret():
#     return cal
#
# y = ret()
# print(y.add(2, 4))
# import cal as model_cal
# import communication as comm
# cal = 100
# print(model_cal.x)
# print(model_cal.add)
# print(model_cal.sub(2, 5))
# print(comm.send_sms())
# print(comm.x)
# 版本1
# import cal
# print(cal.add(1, 2))
# print(cal.sub(1, 2))
# print(cal.mul(1, 2))
# print(cal.div(1, 2))
# 版本2: from 模块名 import 变量
# from cal import add, sub, mul, div
# from cal import *  # 不推荐
# # print(cal.add(1, 2))
# print(add(1, 2))
# print(sub(1, 2))
# print(mul(1, 2))
# print(div(1, 2))
# from cal import add as model_add
# from cal import asdfghjkl as asd
# add = 100
# print(model_add(1, 2))
# print(asd)

# import cal
# import communication
# import mysql
# print(cal.div(10, 2))
# print(__name__)  # __main__
from mysql import mysql_init
from cal import *
mysql_init()
