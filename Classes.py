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
    def __init__(self, name, hp, atk, defense, level, xp, crit_chance, gold, goldgain):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.level = level
        self.xp = xp
        self.crit_chance = crit_chance
        self.gold = gold
        self.goldgain = goldgain

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

    def set_attack(self, atk):
        self.atk = atk

    def get_defense(self):
        return self.defense

    def set_defense(self, defense):
        self.defense = defense

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

    def get_goldgain(self):
        return self.goldgain

    def set_goldgain(self, goldgain):
        self.goldgain = goldgain

    def level_up(self):
        self.level += 1
        self.hp = int(100 + ((40 * self.level) ** 1.1))
        self.atk = int(15 + ((12 * self.level) ** 1.1))
        self.defense = int(10 + ((6 * self.level) ** 1.1))

    def draw_hp_bar(self, screen, x, y, width, height):
        pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
        hp_width = self.hp / self.get_max_hp() * width
        pygame.draw.rect(screen, (0, 255, 0), (x, y, hp_width, height))


class ShopItem:
    def __init__(self, name, price, atk, defense, crit_chance, hp, goldgain, rect, hovertext):
        self.name = name
        self.price = price
        self.atk = atk
        self.defense = defense
        self.crit_chance = crit_chance
        self.hp = hp
        self.goldgain = goldgain
        self.rect = rect
        self.hovertext = hovertext

    def draw(self, screen, font):
        pygame.draw.rect(screen, (120, 120, 0), self.rect)
        screen.blit(font.render(self.name, 1, (10, 10, 10)), (self.rect.x + 10, self.rect.y + 10))
        screen.blit(font.render(f"Price: {self.price}", 1, (10, 10, 10)), (self.rect.x + 10, self.rect.y + 40))

    def draw_hover_text(self, screen, font, mouse_pos):
        #hover_text = f"{self.name}: {self.price} gold"
        text_surface = font.render(self.hovertext, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (mouse_pos[0] + 10, mouse_pos[1] + 10)
        pygame.draw.rect(screen, (0, 0, 0), text_rect.inflate(10, 10))
        screen.blit(text_surface, text_rect)

def draw_shop_items(screen, items, font, start_position, box_size, spacing):
    x, y = start_position
    shop_item_objects = []
    for index, item in enumerate(items):
        rect = pygame.Rect(x, y, box_size[0], box_size[1])
        shop_item = ShopItem(item['name'], item['price'], item['atk'], item['defense'], item['crit_chance'], item['hp'], item['goldgain'], rect, item['hovertext'])
        shop_item.draw(screen, font)
        shop_item_objects.append(shop_item)
        x += box_size[0] + spacing
        if (index + 1) % 5 == 0:
            x = start_position[0]
            y += box_size[1] + spacing
    return shop_item_objects

def handle_shop_click(shop_items, event, Knight1):
    for item in shop_items:
        if item.rect.collidepoint(event.pos):
            if Knight1.get_gold() >= item.price:
                Knight1.set_gold(Knight1.get_gold() - item.price)
                print(f"Bought {item.name} for {item.price} gold.")
                Knight1.set_attack(Knight1.get_attack() * max(item.atk, 1))
                Knight1.set_defense(Knight1.get_defense() * max(item.defense, 1))
                Knight1.set_crit_chance(Knight1.get_crit_chance() + max(item.crit_chance, 1))
                Knight1.set_hp(Knight1.get_hp() + max(item.hp, 1))
                Knight1.set_goldgain(Knight1.get_goldgain() + max(item.goldgain, 1))
                return item.name
            else:
                print("Not enough gold!")
                return None


def handle_shop_hover(shop_items, screen, font, mouse_pos):
    for item in shop_items:
        if item.rect.collidepoint(mouse_pos):
            item.draw_hover_text(screen, font, mouse_pos)
            break
