class Boss():
    def __init__(self, name, hp, atk, defense, level):
        self.name = name
        self.hp = hp + (90 * level)
        self.atk = atk + (9 * level)
        self.defense = defense + (6 * level)
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
        pass


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

    def get_xp(self):
        return self.xp

    def set_xp(self, xp):
        self.xp = xp

    def kill(self):
        pass
