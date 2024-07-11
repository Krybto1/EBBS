import random
import main

lvlup_boss = random.randint(1, 3)

class Boss():
    def __init__(self, name, hp, atk, defense, level):
        self.name = name
        self.hp = hp + (75 * level)
        self.atk = atk + (4 * level)
        self.defense = defense + (2 * level)
        self.level = level

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp


    def get_attack(self):
        return self.atk

    def set_attack(self, atk):
        self.atk = atk

    def get_defense(self):
        return self.defense

    def get_level(self):
        return self.level

    def kill(self):
        xp_grab = self.level * 100
        self.level += lvlup_boss
        self.hp = self.hp + (75 * self.level)
        self.atk = self.atk + (4 * self.level)
        self.defense = self.defense + (2 * self.level)
        return xp_grab

class Knight():
    def __init__(self, name, hp, atk, defense, level, xp):
        self.name = name
        self.hp = hp + (75 * level)
        self.atk = atk + (7 * level)
        self.defense = defense + (4 * level)
        self.level = level
        self.xp = xp

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp

    def get_attack(self):
        return self.atk

    def get_defense(self):
        return self.defense

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level

    def get_xp(self):
        return self.xp

    def set_xp(self, xp):
        self.xp = xp

    def level_up(self):
        self.xp = (self.get_xp() - main.Player_XP_Thr)
        self.level = (self.get_level() + 1)
        Knight1.set_hp = Base_Knight_HP + (75 * Knight1.level)
        Knight1.set_atk = Base_Knight_ATK + (7 * Knight1.level)
        Knight1.set_defense = Base_Knight_DEF + (4 * Knight1.level)
