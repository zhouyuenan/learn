# ------------------------------------------------
# Program:
#       This program is used to learn python grammar.
#       此脚本用于学习python语法
# History:
#       2023/08/02 周月南 First release
# ------------------------------------------------
def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
