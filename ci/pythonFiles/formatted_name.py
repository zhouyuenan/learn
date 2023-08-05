# ------------------------------------------------
# Program:
#       This program is used to learn python grammar.
#       此脚本用于学习python语法
# History:
#       2023/08/05 周月南 First release
# ------------------------------------------------
# def get_formatted_name(first_name, middle_name, last_name):
#     """返回整洁的姓名。"""
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名。"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
