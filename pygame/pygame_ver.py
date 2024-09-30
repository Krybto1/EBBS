import time
import pygame
from Classes import Boss, Knight, ShopItem
import Classes
import misc2
import random
import os
import loader

shop_items = loader.load("items.json")

CharName = input("Enter your character name: ")
Knight1 = Knight(CharName, 100, 15, 10, 1, 0, 10, 21000, 1)
Boss1 = Boss(f"{misc2.rarity_tiers[0]} {'Goblin'}", 75, 13, 5, 1)


def shake_image(screen, image, position, shake_intensity, shake_duration, bg_color):
    end_time = time.time() + shake_duration
    original_position = position
    image_rect = image.get_rect(topleft=original_position)

    while time.time() < end_time:
        offset_x = random.randint(-shake_intensity, shake_intensity)
        new_position = (original_position[0] + offset_x, original_position[1])

        # Fill the old position with the background color
        screen.fill(bg_color, image_rect)

        # Draw the image at the new position
        screen.blit(image, new_position)
        pygame.display.flip()
        time.sleep(0.05)

        # Update the image_rect to the new position
        image_rect.topleft = new_position


def enter_shop(screen, shop_screen, font, Knight1, Shop_Exit_Button, bg_line):
    global shop_active, shop_items
    shop_active = True
    while shop_active:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if Shop_Exit_Button.is_clicked(event):
                shop_active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                item_name = Classes.handle_shop_click(shop_item_objects, event, Knight1)
                if item_name:
                    item = loader.get_item_by_name(shop_items, item_name)
                    if item:
                        item["price"] = int(item["price"] * item["pricemodifier"])

        shop_screen.fill((230, 230, 230))
        shop_screen.blit(font.render(f"Welcome to the Shop!", 1, (10, 10, 10)), (500, 40))
        shop_screen.blit(font.render(f"Current Gold: {Knight1.get_gold()}", 1, (10, 10, 10)), (500, 80))
        Shop_Exit_Button.draw(shop_screen)

        # Draw background boxes for shop items
        shop_item_objects = Classes.draw_shop_items(shop_screen, shop_items, font, (100, 150), (150, 150), 50)

        # Handle hover text
        Classes.handle_shop_hover(shop_item_objects, shop_screen, font, mouse_pos)

        screen.blit(shop_screen, (0, 0))
        shop_screen.blit(bg_line, (0, 590))
        pygame.display.flip()

def main():
    screen = pygame.display.set_mode((1200, 800))
    shop_screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Epic Boss Battle Simulator")
    clock = pygame.time.Clock()
    running = True
    dt = 0
    Turn = 0
    Floor = 1
    Kill_Count = 0
    Scale = 1
    ItemsBonus = 0
    shop_active = False

    pygame.init()
    font_loader = "C:/Windows/Fonts/Calibri.ttf"
    Boss_Choices = ("Attack", "Defend", "Sleep")
    img_enemy = pygame.image.load("img/Goblin_Test.jpg")
    img_sword = pygame.image.load("img/Sword_Icon.png")
    img_sword = pygame.transform.scale(img_sword, (75, 75))
    img_shield = pygame.image.load("img/Shield_Icon.png")
    img_shield = pygame.transform.scale(img_shield, (75, 75))
    img_sleep = pygame.image.load("img/Sleep_Icon.png")
    img_sleep = pygame.transform.scale(img_sleep, (75, 75))
    bg_line = pygame.image.load("img/Bg_Line.png")
    img_gold = pygame.image.load("img/Gold_Icon.jpg")
    img_gold = pygame.transform.scale(img_gold, (50, 50))

    font = pygame.font.Font(font_loader, 27)
    Atk_Button = misc2.Button(500, 100, 150, 50, "Attack", (170, 0, 0), (200, 100, 0))
    Def_Button = misc2.Button(500, 175, 150, 50, "Defend", (0, 0, 170), (0, 100, 200))
    Sleep_Button = misc2.Button(500, 250, 150, 50, "Sleep", (170, 0, 170), (200, 0, 200))
    Shop_Button = misc2.Button(1050, 530, 150, 50, "Shop", (255, 255, 0), (255, 255, 100))
    Shop_Exit_Button = misc2.Button(1050, 600, 150, 50, "Exit", (0, 255, 0), (0, 255, 100))

    while running:
        screen.blit(bg_line, (0, 590))
        crit_rdm = random.randint(1, 100)
        boss_name = font.render(Boss1.get_name(), 1, (10, 10, 10))
        boss_pos = boss_name.get_rect(centerx=1000, centery=375)
        img_enemy = pygame.transform.scale(img_enemy, (200, 200))
        boss_heal = (Boss1.get_level() * 2) * 1.5

        player_name = font.render(Knight1.get_name(), 1, (10, 10, 10))
        player_pos = player_name.get_rect(centerx=200, centery=375)
        img_player = pygame.image.load("img/Player_Img.jpg")
        bg_line = pygame.transform.scale(bg_line, (screen.get_width(), 2))

        img_player = pygame.transform.scale(img_player, (200, 200))
        player_heal = (Knight1.get_level() * 5) * 1.5
        Player_XP_Thr = int((80 * Knight1.get_level()) ** 1.07)
        XP_check = Knight1.get_xp()
        while XP_check >= Player_XP_Thr:
            Knight1.set_xp(XP_check - Player_XP_Thr)
            Knight1.level_up()
            XP_check = Knight1.get_xp()

        XP_check2 = Knight1.get_xp()
        Player_XP_Thr = int((80 * Knight1.get_level()) ** 1.07)
        boss_choice = random.choice(Boss_Choices)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if Shop_Button.is_clicked(event):
                enter_shop(screen, shop_screen, font, Knight1, Shop_Exit_Button, bg_line)
            if Atk_Button.is_clicked(event):
                screen.blit(img_sword, (350, 175))
                player_crit = 0
                if crit_rdm <= Knight1.crit_chance:
                    player_crit = True
                if boss_choice == "Defend":
                    screen.blit(img_shield, (725, 175))
                    if player_crit:
                        Boss1.set_hp(int(Boss1.get_hp() - (((Knight1.get_attack() - Boss1.get_defense()) / 2) * 1.75)))
                        screen.blit(font.render(
                            f"ITS A CRIT! {Knight1.get_name()} attacks {Boss1.get_name()} for {int(((Knight1.get_attack() - Boss1.get_defense()) / 2) * 1.75)} damage",
                            1, (255, 10, 10)), (200, 600))
                        screen.blit(font.render(
                            f"{Boss1.get_name()} defends and blocks {int(((Knight1.get_attack() - Boss1.get_defense()) / 2) * 1.75)} damage",
                            1, (0, 0, 255)), (200, 630))
                    else:
                        screen.blit(font.render(
                            f"{Knight1.get_name()} attacks {Boss1.get_name()} for {Knight1.get_attack() - Boss1.get_defense()} damage",
                            1, (255, 10, 10)), (200, 600))
                        screen.blit(font.render(
                            f"{Boss1.get_name()} defends and blocks {(Knight1.get_attack() - Boss1.get_defense()) / 2} damage",
                            1, (0, 0, 255)), (200, 630))
                        Boss1.set_hp(Boss1.get_hp() - ((Knight1.get_attack() - Boss1.get_defense()) / 2))
                elif boss_choice == "Attack":
                    screen.blit(img_sword, (725, 175))
                    Knight1.set_hp(Knight1.get_hp() - (Boss1.get_attack() - Knight1.get_defense()))
                    if player_crit:
                        Boss1.set_hp(int(Boss1.get_hp() - ((Knight1.get_attack() - Boss1.get_defense()) * 1.75)))
                        screen.blit(font.render(
                            f"ITS A CRIT! {Knight1.get_name()} attacks {Boss1.get_name()} for {int((Knight1.get_attack() - Boss1.get_defense()) * 1.75)} damage",
                            1, (255, 10, 10)), (200, 600))
                        screen.blit(font.render(
                            f"{Boss1.get_name()} attacks {Knight1.get_name()} for {Boss1.get_attack() - Knight1.get_defense()} damage",
                            1, (255, 0, 0)), (200, 630))
                        shake_image(screen, img_player, (100, 100), shake_intensity=10, shake_duration=0.5,
                                    bg_color=(230, 230, 230))
                    else:
                        Knight1.set_hp(Knight1.get_hp() - (Boss1.get_attack() - Knight1.get_defense()))
                        Boss1.set_hp(Boss1.get_hp() - (Knight1.get_attack() - Boss1.get_defense()))
                        screen.blit(font.render(
                            f"{Knight1.get_name()} attacks {Boss1.get_name()} for {Knight1.get_attack() - Boss1.get_defense()} damage",
                            1, (255, 10, 10)), (200, 600))
                        screen.blit(font.render(
                            f"{Boss1.get_name()} attacks {Knight1.get_name()} for {Boss1.get_attack() - Knight1.get_defense()} damage",
                            1, (255, 0, 0)), (200, 630))
                        shake_image(screen, img_player, (100, 100), shake_intensity=10, shake_duration=0.5,
                                    bg_color=(230, 230, 230))
                else:
                    screen.blit(img_sleep, (725, 175))
                    if player_crit:
                        screen.blit(font.render(
                            f"ITS A CRIT! {Knight1.get_name()} attacks {Boss1.get_name()} for {int(((Knight1.get_attack() - Boss1.get_defense()) * 1.75))} damage",
                            1, (255, 10, 10)), (200, 600))
                        if Boss1.get_hp() == Boss1.get_max_hp():
                            screen.blit(font.render(f"{Boss1.get_name()} is already at max HP!", 1, (255, 0, 255)),
                                        (200, 630))
                            Boss1.set_hp(int(Boss1.get_hp() - ((Knight1.get_attack() - Boss1.get_defense()) * 1.75)))
                        elif Boss1.get_hp() + boss_heal > Boss1.get_max_hp():
                            Boss1.set_hp(Boss1.get_max_hp())
                            screen.blit(font.render(f"{Boss1.get_name()} sleeps but is almost at max HP!"
                                                    f"Only healed for {(Boss1.get_hp() + boss_heal) - Boss1.get_max_hp()}",
                                                    1, (255, 0, 255)), (200, 630))
                            Boss1.set_hp(int(Boss1.get_hp() - ((Knight1.get_attack() - Boss1.get_defense()) * 1.75)))
                        else:
                            Boss1.set_hp(Boss1.get_hp() + boss_heal)
                            screen.blit(font.render(f"{Boss1.get_name()} sleeps and heals for {boss_heal} HP", 1,
                                                    (255, 0, 255)), (200, 630))
                            Boss1.set_hp(int(Boss1.get_hp() - ((Knight1.get_attack() - Boss1.get_defense()) * 1.75)))
                    else:
                        screen.blit(font.render(f"{Knight1.get_name()} attacks {Boss1.get_name()} for {Knight1.get_attack() - Boss1.get_defense()} damage", 1, (255, 10, 10)), (200, 600))
                        if Boss1.get_hp() == Boss1.get_max_hp():
                            screen.blit(font.render(f"{Boss1.get_name()} is already at max HP!", 1, (255, 0, 255)), (200, 630))
                            Boss1.set_hp(Boss1.get_hp() - (Knight1.get_attack() - Boss1.get_defense()))
                        elif Boss1.get_hp() + boss_heal > Boss1.get_max_hp():
                            Boss1.set_hp(Boss1.get_max_hp())
                            screen.blit(font.render(f"{Boss1.get_name()} sleeps but is almost at max HP!"
                                                    f"Only healed for {(Boss1.get_hp() + boss_heal) - Boss1.get_max_hp() }", 1, (255, 0, 255)), (200, 630))
                            Boss1.set_hp(Boss1.get_hp() - (Knight1.get_attack() - Boss1.get_defense()))
                        else:
                            Boss1.set_hp(Boss1.get_hp() + boss_heal)
                            screen.blit(font.render(f"{Boss1.get_name()} sleeps and heals for {boss_heal} HP", 1, (255, 0, 255)), (200, 630))
                            Boss1.set_hp(Boss1.get_hp() - (Knight1.get_attack() - Boss1.get_defense()))
                shake_image(screen, img_enemy, (900, 100), shake_intensity=10, shake_duration=0.5,
                            bg_color=(230, 230, 230))
            if Def_Button.is_clicked(event):
                screen.blit(img_shield, (350, 175))
                if boss_choice == "Defend":
                    screen.blit(img_shield, (725, 175))
                    screen.blit(font.render(f"{Knight1.get_name()} and {Boss1.get_name()} both defend", 1, (0, 0, 255)), (200, 600))
                elif boss_choice == "Sleep":
                    screen.blit(img_sleep, (725, 175))
                    screen.blit(font.render(f"{Knight1.get_name()} defends but there is no damage to block", 1, (0, 0, 255)), (200, 600))
                    boss_heal = (Boss1.get_level() * 2) * 1.5
                    if Boss1.get_hp() == Boss1.get_max_hp():
                        screen.blit(font.render(f"{Boss1.get_name()} is already at max HP!", 1, (255, 0, 255)), (200, 630))
                    elif Boss1.get_hp() + boss_heal > Boss1.get_max_hp():
                        Boss1.set_hp(Boss1.get_max_hp())
                        screen.blit(font.render(f"{Boss1.get_name()} sleeps but is almost at max HP!"
                                                f"Only healed for {(Boss1.get_hp() + boss_heal) - Boss1.get_max_hp() }", 1, (255, 0, 255)), (200, 630))
                    else:
                        Boss1.set_hp(Boss1.get_hp() + boss_heal)
                        screen.blit(font.render(f"{Boss1.get_name()} sleeps and heals for {boss_heal} HP", 1, (255, 0, 255)), (200, 630))

                else:
                    screen.blit(img_sword, (725, 175))
                    screen.blit(font.render(f"{Knight1.get_name()} defends and blocks {(Boss1.get_attack() - Knight1.get_defense()) / 2} damage", 1, (0, 0, 255)), (200, 600))
                    screen.blit(font.render(f"{Boss1.get_name()} attacks {Knight1.get_name()} for {(Boss1.get_attack() - Knight1.get_defense())} damage", 1, (255, 0, 0)), (200, 630))
                    Knight1.set_hp(Knight1.get_hp() - ((Boss1.get_attack() - Knight1.get_defense()) / 2))
                    shake_image(screen, img_player, (100, 100), shake_intensity=10, shake_duration=0.5, bg_color=(230, 230, 230))
            if Sleep_Button.is_clicked(event):
                screen.blit(img_sleep, (350, 175))
                if Knight1.get_hp() == Knight1.get_max_hp():
                    screen.blit(font.render(f"{Knight1.get_name()} is already at max HP!", 1, (255, 0, 255)), (200, 600))
                elif Knight1.get_hp() + player_heal > Knight1.get_max_hp():
                    Knight1.set_hp(Knight1.get_max_hp())
                    screen.blit(font.render(f"{Knight1.get_name()} sleeps but is almost at max HP!"
                                            f"Only healed for {(Knight1.get_hp() + player_heal) - Knight1.get_max_hp()}", 1, (255, 0, 255)), (200, 600))
                else:
                    screen.blit(font.render(f"{Knight1.get_name()} sleeps and heals for {player_heal} HP", 1, (255, 0, 255)), (200, 600))
                    Knight1.set_hp(Knight1.get_hp() + player_heal)
                if boss_choice == "Defend":
                    screen.blit(img_shield, (725, 175))
                    screen.blit(font.render(f"{Boss1.get_name()} defends but there is no damage to block", 1, (0, 0, 255)), (200, 630))
                elif boss_choice == "Attack":
                    screen.blit(img_sword, (725, 175))
                    screen.blit(font.render(f"{Boss1.get_name()} attacks {Knight1.get_name()} for {Boss1.get_attack() - Knight1.get_defense()} damage", 1, (255, 0, 0)), (200, 630))
                    Knight1.set_hp(Knight1.get_hp() - (Boss1.get_attack() - Knight1.get_defense()))
                    shake_image(screen, img_player, (100, 100), shake_intensity=10, shake_duration=0.5, bg_color=(230, 230, 230))
                else:
                    screen.blit(img_sleep, (725, 175))
                    if Boss1.get_hp() == Boss1.get_max_hp():
                        screen.blit(font.render(f"{Boss1.get_name()} is already at max HP!", 1, (255, 0, 255)),
                                    (200, 630))
                    elif Boss1.get_hp() + boss_heal > Boss1.get_max_hp():
                        Boss1.set_hp(Boss1.get_max_hp())
                        screen.blit(font.render(f"{Boss1.get_name()} sleeps but is almost at max HP!"
                                                f"Only healed for {(Boss1.get_hp() + boss_heal) - Boss1.get_max_hp()}",
                                                1, (255, 0, 255)), (200, 630))
                    else:
                        Boss1.set_hp(Boss1.get_hp() + boss_heal)
                        screen.blit(
                            font.render(f"{Boss1.get_name()} sleeps and heals for {boss_heal} HP", 1, (255, 0, 255)),
                            (200, 630))

            pygame.display.flip()

        time.sleep(0.75)
        screen.fill((230, 230, 230))
        screen.blit(font.render(f"Floor {Floor} Turn {Turn}", 1, (10, 10, 10)), (500, 40))

        screen.blit(boss_name, boss_pos)
        screen.blit(img_enemy, (900, 100))
        Boss1.draw_hp_bar(screen, 900, 300, 200, 25)
        screen.blit(font.render(f"HP: {max(int(Boss1.get_hp()), 0)}", 1, (10, 10, 10)), (930, 300))
        screen.blit(font.render(f"Stats", 1, (10, 10, 10)), (900, 400))
        screen.blit(font.render(f"Attack: {int(Boss1.get_attack())}", 1, (170, 0, 0)), (900, 430))
        screen.blit(font.render(f"Defense: {int(Boss1.get_defense())}", 1, (0, 0, 170)), (900, 460))
        screen.blit(font.render(f"Level: {Boss1.get_level()}", 1, (170, 0, 170)), (900, 490))

        screen.blit(player_name, player_pos)
        Knight1.draw_hp_bar(screen, 100, 300, 200, 25)
        screen.blit(font.render(f"HP: {max(int(Knight1.get_hp()), 0)}", 1, (10, 10, 10)), (130, 300))
        screen.blit(font.render(f"XP: {XP_check2} /// {Player_XP_Thr}", 1, (0, 255, 0)), (100, 325))
        screen.blit(font.render(f"Stats", 1, (10, 10, 10)), (100, 400))
        screen.blit(font.render(f"Attack: {int(Knight1.get_attack() + ItemsBonus)}", 1, (170, 0, 0)), (100, 430))
        screen.blit(font.render(f"Defense: {int(Knight1.get_defense())}", 1, (0, 0, 170)), (100, 460))
        screen.blit(font.render(f"Level: {Knight1.get_level()}", 1, (170, 0, 170)), (100, 490))
        screen.blit(font.render(f"Crit Chance: {Knight1.get_crit_chance()}%", 1, (255, 0, 255)), (100, 520))
        screen.blit(font.render(f"Gold: {Knight1.get_gold()}", 1, (230, 230, 80)), (100, 550))
        screen.blit(img_player, (100, 100))

        Atk_Button.draw(screen)
        Def_Button.draw(screen)
        Sleep_Button.draw(screen)
        Shop_Button.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)

        if Boss1.get_hp() <= 0:
            screen.blit(font.render(f"{Knight1.get_name()} has defeated {Boss1.get_name()} !", 1, (0, 255, 0)), (200, 690))
            screen.blit(font.render(f"Gained {int((Boss1.get_xp() * Scale))} XP and {int(((7 * Floor) * Scale) * Knight1.goldgain)} Gold!", 1, (0, 255, 0)), (200, 720))
            Knight1.set_xp(int(Knight1.get_xp() + (Boss1.get_xp() * Scale)))
            get_gold = Knight1.get_gold()
            Knight1.set_gold(int(get_gold + (((7 * Floor) * Scale) * Knight1.goldgain)))
            Boss1.kill()
            if Floor > 5:
                Rarity_Choice = random.choices(misc2.rarity_tiers,
                                           weights=[0.3, 0.2, 0.1, 0.04, 0.04, 0.03, 0.03, 0.03,
                                                    0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                                                    0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                                                    0.01, 0.01, 0.01, 0.01, 0.01], k=1)
                Scale = misc2.rarity_scale[Rarity_Choice[0]]
                Boss1.set_name(f"{Rarity_Choice[0]} {random.choice(misc2.enemies)}")
            else:
                Rarity_Choice = misc2.rarity_tiers[0]
                Scale = 1
                Boss1.set_name(f"{Rarity_Choice} {random.choice(misc2.enemies)}")

            boss_index = misc2.enemies.index(Boss1.get_name().split(maxsplit=1)[1])
            if os.path.exists(misc2.enemies_png[boss_index]):
                img_enemy = pygame.image.load(misc2.enemies_png[boss_index])
            else:
                img_enemy = pygame.image.load("img/Goblin_Test.jpg")
            Boss1.set_max_hp(Scale)
            Boss1.set_hp(int(Boss1.get_hp() * Scale))
            Boss1.set_attack(int(Boss1.get_attack() * Scale))
            Boss1.set_defense(int(Boss1.get_defense() * Scale))
            Kill_Count += 1
            Floor += 1
            Turn = 0
        elif Knight1.get_hp() <= 0:
            screen.blit(font.render(f"{Knight1.get_name()} has been defeated by {Boss1.get_name()} !", 1, (255, 0, 0)), (200, 690))
            screen.blit(font.render(f"Killcount: {Kill_Count}           Game Over!", 1, (255, 0, 0)), (200, 720))
            pygame.display.flip()
            time.sleep(5)
            running = False
        pygame.display.flip()


if __name__ == "__main__": main()
