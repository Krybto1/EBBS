import random


class Boss:
    def __init__(self, name, hp, atk, defense, level):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.level = level

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp

    def set_name(self, name):
        self.name = name


    def get_attack(self):
        return self.atk

    def set_attack(self, atk):
        self.atk = atk

    def get_defense(self):
        return self.defense

    def set_defense(self, defense):
        self.defense = defense

    def get_level(self):
        return self.level

    def kill(self):
        lvlup_boss = random.randint(1, 4)
        self.level += lvlup_boss
        self.hp = int(75 + ((20 * self.level) ** 1.02))
        self.atk = int(12 + ((7 * self.level) ** 1.02))
        self.defense = int(7 + ((4 * self.level) ** 1.02))

    def get_xp(self):
        xp_grabber = self.level * (100 ** 1.07)
        return xp_grabber


class Knight:
    def __init__(self, name, hp, atk, defense, level, xp):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
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
        self.level += 1
        self.hp = int(100 + ((40 * self.level) ** 1.1))
        self.atk = int(15 + ((12 * self.level) ** 1.1))
        self.defense = int(10 + ((6 * self.level) ** 1.1))

