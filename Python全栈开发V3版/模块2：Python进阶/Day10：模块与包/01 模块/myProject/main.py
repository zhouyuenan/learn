import cal
import communication
import mysql
def two_value_cal():
    exp = input("请输入双值计算表达式：")
    if exp.find("+") != -1:
        a, b = exp.split("+")
        print(f"{a}+{b}={cal.add(int(a), int(b))}")
    elif exp.find("-") != -1:
        a, b = exp.split("-")
        print(f"{a}-{b}={cal.sub(int(a), int(b))}")
    elif exp.find("*") != -1:
        a, b = exp.split("*")
        print(f"{a}*{b}={cal.mul(int(a), int(b))}")
    elif exp.find("/") != -1:
        a, b = exp.split("/")
        print(f"{a}/{b}={cal.div(int(a), int(b))}")
    elif exp.find("cf") != -1:
        a, b = exp.split("cf")
        print(f"{a}**{b}={cal.my_pow(int(a), int(b))}")
while 1:
    print("1. 科学计算")
    print("2. 数据库操作")
    print("3. 通信操作")
    choice = input("请选择：")
    if choice == "1":
        two_value_cal()
    elif choice == "2":
        action = input("""
            请选择如下数据库操作：
            1. 添加记录
            2. 删除记录
            3. 修改记录
            4. 查询记录
        """)
        if action == "1":
            mysql.mysql_init()
            mysql.mysql_insert()
        elif action == "2":
            mysql.mysql_init()
            mysql.mysql_delete()
        elif action == "3":
            mysql.mysql_init()
            mysql.mysql_update()
        elif action == "4":
            mysql.mysql_init()
            mysql.mysql_query()
    elif choice == "3":
        communication.send_email()
        communication.send_sms()
