import random

import pygame.draw


class Boss:
    def __init__(self, name, hp, atk, defense, level):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.defense = defense
        self.level = level

    def get_name(self):
        return self.name

    def get_hp(self):
        return int(self.hp)

    def set_hp(self, hp):
        self.hp = hp

    def set_max_hp(self, scale):
        self.max_hp = int((75 + ((20 * self.level) ** 1.02)) * scale) if self.level > 1 else 75

    def get_max_hp(self):
        return self.max_hp

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

    def draw_hp_bar(self, screen, x, y, width, height):
        pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
        hp_width = self.hp / self.get_max_hp() * width
        pygame.draw.rect(screen, (0, 255, 0), (x, y, hp_width, height))

class Knight:
    def __init__(self, name, hp, atk, defense, level, xp, crit_chance, gold):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.level = level
        self.xp = xp
        self.crit_chance = crit_chance
        self.gold = gold

    def get_name(self):
        return self.name

    def get_hp(self):
        return int(self.hp)

    def get_max_hp(self):
        return int(100 + ((40 * self.level) ** 1.1) if self.level > 1 else 100)

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

    def get_crit_chance(self):
        return self.crit_chance

    def set_crit_chance(self, crit_chance):
        self.crit_chance = crit_chance


    def get_gold(self):
        return self.gold

    def set_gold(self, gold):
        self.gold = gold

    def level_up(self):
        self.level += 1
        self.hp = int(100 + ((40 * self.level) ** 1.1))
        self.atk = int(15 + ((12 * self.level) ** 1.1))
        self.defense = int(10 + ((6 * self.level) ** 1.1))

    def draw_hp_bar(self, screen, x, y, width, height):
        pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
        hp_width = self.hp / self.get_max_hp() * width
        pygame.draw.rect(screen, (0, 255, 0), (x, y, hp_width, height))

