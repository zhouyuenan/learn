# from calendar import month_name
#
# edward = ['Edward', 42]
# john = ['John Smith', 50]
# database = [edward, john]
# print(database)
# greeting = 'Hello'
# print(greeting[0])
# print(greeting[-1])
# print('Hello'[1])
# fourth = input('Year: ')[3]
# print(fourth)
# 将以指定年、月、日的日期打印出来
# months = [
#     'January',
#     'February',
#     'March',
#     'April',
#     'May',
#     'June',
#     'July',
#     'August',
#     'September',
#     'October',
#     'November',
#     'December'
# ]
#
# # 一个列表，其中包含数1-31对应的结尾
# endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
#     + ['st', 'nd', 'rd'] + 7 * ['th'] \
#     + ['st']
# print(endings)
# year = input('Year: ')
# month = input('Month (1-12): ')
# day = input('Day (1-12): ')
#
# month_number = int(month)
# day_number = int(day)
#
# # 别忘了将表示月和日的数减1，这样才能得到正确的索引
# month_name = months[month_number-1]
# ordinal = day + endings[day_number-1]
#
# print(month_name + ' ' + ordinal + ', ' + year)
from setuptools.dist import sequence

tag = '<a href="http://www.python.org">Python web site</a>'
# print(tag[9:30])
# print(tag[32:-4])
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[3:6])
# print(numbers[0:1])
# print(numbers[7:10])
# print(numbers[-3:-1])
# print(numbers[-3:0])
# print(numbers[-3:])
# print(numbers[:3])
# print(numbers[:])
# url = input('Please enter the URL: ')
# domain = url[11:-4]
# print("Domain name: " + domain)
# print(numbers[0:10:1])
# print(numbers[0:10:2])
# print(numbers[3:6:3])
# print(numbers[::4])
# print(numbers[8:3:-1])
# print(numbers[10:0:-2])
# print(numbers[0:10:-2])
# print(numbers[::-2])
# print(numbers[5::-2])
# print(numbers[:5:-2])
# [1, 2, 3] + [4, 5, 6]
# 'Hello,' + ' world!'
# result = [1, 2, 3] + ' world!'
# 'python' * 5
# [42] * 10
# sequence = [None] * 10
# print(sequence)
# 在位于屏幕中央且宽度合适的方框内打印一个句子
# sentence = input("Sentence: ")
#
# screen_width = 160
# text_width = len(sentence)
# box_width = text_width + 6
# left_margin = (screen_width - box_width) // 2
#
# print()
# print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
# print(' ' * left_margin + '|  ' + ' ' * text_width + '  |')
# print(' ' * left_margin + '|  ' + sentence + '  |')
# print(' ' * left_margin + '|  ' + ' ' * text_width + '  |')
# print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
# print()
#
# print(text_width)
# permission = 'rw'
# 'w' in permission
# 'x' in permission
# users = ['mlh', 'foo', 'bar']
# input('Enter your user name: ') in users
# subject = '$$$ Get rich now!!! $$$'
# '$$$' in subject
# result =  'p' in 'python'
# print(result)
# 检查用户名和PIN码
# database = [
#     ['albert', '1234'],
#     ['dilbert', '4242'],
#     ['smith', '7524'],
#     ['jones', '9843']
# ]
#
# username = input("User name: ")
# pin = input("PIN code: ")
#
# if [username, pin] in database:
#     print('Access granted')
# numbers = [100, 34, 678]
# len(numbers)
# max(numbers)
# min(numbers)
# max(2, 3)
# min(9, 3, 2, 5)
# list('Hello')
# print(list('Hello'))
# x = [1, 1, 1]
# x[1] = 2
# print(x)
# test = ['ha'] * 10
# test[100] = "hei"
# print(test)
# names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
# del names[2]
# print(names)
# print(len(names))
# name = list('Perl')
# print(name)
# name[2:] = list('ar')
# print(name)
# name = list('Perl')
# name[1:] = list('ython')
# print(name)
# numbers = [1, 5]
# numbers[1:1] = [2, 3, 4]
# print(numbers)
# print(numbers)
# # del numbers[1:4]
# # numbers[1:4] = []
# numbers[4::3] = []
# print(numbers)
# lst = [1, 2, 3, 4]
# lst.append(4)
# print(lst)
# lst = [1, 3, 3]
# lst [:] = []
# # lst.clear()
# print(lst)
# a = [1, 2, 3]
# b = a
# b[1] = 4
# print(a)
a = [1, 2, 3]
b = list(a)
b[1] = 4
print(a)
list_test = ['to', 'be', 'or', 'not', 'to', 'be']
times = list_test.count('to')
print(times)