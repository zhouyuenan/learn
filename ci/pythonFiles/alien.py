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
    alien_0 = {'color': 'green'}
    print(f"The alien is {alien_0['color']}.")
    alien_0['color'] = 'yellow'
    print(f"The alien is now {alien_0['color']}.")
def test_2():
    alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
    print(f"Original x_position: {alien_0['x_position']}")
    # 向右移动外星人。
    # 根据当前速度确定将外星人向右移动多远。
    if alien_0['speed'] == 'slow':
        x_increment = 1
    elif alien_0['speed'] == 'medium':
        x_increment = 2
    else:
        # 这个外星人的速度肯定移动很快
        x_increment = 3
    # 新位置为旧位置加上移动距离。
    alien_0['x_position'] = alien_0['x_position'] + x_increment
    print(f"New x_position: {alien_0['x_position']}")
def test_3():
    alien_0['speed'] = 'fast'
def test_4():
    alien_0 = {'color': 'green', 'points': 5}
    print(alien_0)
    del alien_0['points']
    print(alien_0)
def test_5():
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
test_0()
test_1()
test_2()
test_3()
test_4()
test_5()