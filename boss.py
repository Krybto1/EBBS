class Boss():
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
        pass


    def get_attack(self):
        return self.atk

    def get_defense(self):
        return self.defense

    def get_level(self):
        return self.level

    def kill(self):
        pass


class Knight():
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

    def get_attack(self):
        return self.atk

    def get_defense(self):
        return self.defense

    def get_level(self):
        return self.level

    def kill(self):
        pass
