from loguru import logger


class Player(object):

    def __init__(self, name, health=100, gold=100, defense=100, attack=100, level=1, weapon_list=[]):
        self.name = name
        self.health = health
        self.gold = gold
        self.defense_value = defense
        self.attack_value = attack
        self.level = level
        self.weapon_list = weapon_list

    def attack(self, defender, weapon_index = None):
        if weapon_index is None:
            damage = int((self.attack_value - defender.defense_value) / 10)
        else:
            damage = int((self.weapon_list[weapon_index].attack_value - defender.defense_value) / 10)
        if damage > 0:
            defender.health -= damage
            logger.info(f"{self.name}成功攻击了{defender.name}, 造成了{damage}点伤害")
        else:
            logger.info(f"{self.name}的攻击被{defender.name}防御了。")

    def buy_weapon(self, weapon):
        self.weapon_list.append(weapon)
        logger.info(f"{self.name}购买装备{weapon.name}")

    def level_up(self):
        self.level += 1
        self.gold += 100
        logger.info(f"{self.name}升级了, 奖励金币100!")


class Weapon(object):

    def __init__(self, name, attack_value, defense_value):
        self.name = name
        self.attack_value = attack_value
        self.defense_value = defense_value


yuan = Player("yuan")
alex = Player("alex")
weapon1 = Weapon("屠龙刀", 250, 90)
weapon2 = Weapon("倚天剑", 350, 120)
yuan.buy_weapon(weapon1)
yuan.buy_weapon(weapon2)
yuan.attack(alex, 0)
print(alex.health)
yuan.attack(alex, 1)
print(alex.health)
alex.attack(yuan)
# buy_weapon(hero, "屠龙刀")
# attack(hero, enemy)
# attack(hero, enemy)
# attack(enemy, hero)
# level_up(hero)
