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
tag = '<a href="http://www.python.org">Python web site</a>'
print(tag[9:30])
print(tag[32:-4])
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:6])
print(numbers[0:1])
