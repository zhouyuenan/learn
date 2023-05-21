#! python3
# ------------------------------------------------
# Program:
#       This program is used to learn python grammar.
#       此脚本用于学习python语法
# History:
#       2023/02/10 周月南 First release
#       2023/03/23 周月南 Second release
#       2023/03/24 周月南 Third release
# ------------------------------------------------
import openpyxl
import os
import this
import webbrowser


webbrowser.open('https://git-scm.com/')
wb = openpyxl.load_workbook('test.xlsx')


def build_test():
    tests = ['test1', 'test2', 'test3']
    for test in tests:
        print(test)
    # os.makedirs()


build_test()
