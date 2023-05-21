# ------------------------------------------------
# Program:
#       This program is used to learn python grammar.
#       此脚本用于学习python语法
# History:
#       2023/05/21 周月南 First release
# ------------------------------------------------
def test_0():
    alien_0 = {'color': 'green', 'speed': 'slow'}
    point_value = alien_0.get('points', 'No point value assigned.')
    print(point_value)
test_0()