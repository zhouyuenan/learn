# ------------------------------------------------
# Program:
#       This program is used to learn python grammar.
#       此脚本用于学习python语法
# History:
#       2023/08/05 周月南 First release
# ------------------------------------------------
# age = 12
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $25.")
# else:
#     print("Your admission cost is $40.")
# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40
# print(f"Your admission cost is ${price}.")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}")
