# ------------------------------------------------
# Program:
#       This program is used to learn python grammar.
#       此脚本用于学习python语法
# History:
#       2023/05/21 周月南 First release
# ------------------------------------------------
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
alien_0 = {'color': 'green'}
print(alien_0['color'])


def test_0():
    alien_0 = {}
    alien_0['color'] = 'green'
    alien_0['points'] = 5
    print(alien_0)
def test_1():

test_0()
test_1()