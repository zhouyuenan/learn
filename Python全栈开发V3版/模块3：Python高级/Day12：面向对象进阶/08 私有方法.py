# class AirConditioner:
#
#     def __init__(self):
#         # 初始化空调
#         pass
#
#     def cool(self, temperature):
#         # 对外制冷功能接口方法
#         self.__turn_on_compressor()
#         self.__set_temperature(temperature)
#         self.__blow_cold_air()
#         self.__turn_off_compressor()
#
#     @staticmethod
#     def __turn_on_compressor():
#         # 打开压缩机 (私有方法)
#         print("打开压缩机")
#
#     @staticmethod
#     def __set_temperature(temperature):
#         # 设置温度 (私有方法)
#         print("设置温度")
#
#     @staticmethod
#     def __blow_cold_air():
#         # 吹冷气 (私有方法)
#         print("吹冷气")
#
#     @staticmethod
#     def __turn_off_compressor():
#         # 关闭压缩机 (私有方法)
#         print("关闭压缩机")
#
#
# ac = AirConditioner()
# ac.cool(30)
# # ac.__blow_cold_air()
# ac._AirConditioner__blow_cold_air()
# print(dir(ac))
# print(ac.__dict__)
# print(dir(AirConditioner))


# 案例
class Base(object):

    def __foo(self):
        print("foo from Base")

    def test(self):
        self.__foo()  # self._Base__foo()


class Son(Base):

    def __foo(self):
        print("foo from Son")


s = Son()
# s.foo = 100
s.test()