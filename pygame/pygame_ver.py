import time

import pygame
from boss import Boss
from boss import Knight
import misc2
import random
import os


CharName = input("Enter your character name: ")
Knight1 = Knight(CharName, 100, 15, 10, 1, 0)
Boss1 = Boss(f"{misc2.rarity_tiers[0]} {'Goblin'}", 75, 13, 5, 1)

def main():
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Epic Boss Battle Simulator")
    clock = pygame.time.Clock()
    running = True
    dt = 0
    Turn = 0
    Floor = 1
    Kill_Count = 0
    Scale = 1

    pygame.init()
    font_loader = "C:/Windows/Fonts/Calibri.ttf"
    Boss_Choices = ("Attack", "Defend", "Sleep")
    img_enemy = pygame.image.load("img/goblin_test.jpg")
    font = pygame.font.Font(font_loader, 27)
    Atk_Button = misc2.Button(500, 100, 150, 50, "Attack", (170, 0, 0), (200, 100, 0))
    Def_Button = misc2.Button(500, 175, 150, 50, "Defend", (0, 0, 170), (0, 100, 200))
    Sleep_Button = misc2.Button(500, 250, 150, 50, "Sleep", (170, 0, 170), (200, 0, 200))

    while running:
        boss_name = font.render(Boss1.get_name(), 1, (10, 10, 10))
        boss_pos = boss_name.get_rect(centerx=1000, centery=350)
        img_enemy = pygame.transform.scale(img_enemy, (200, 200))
        boss_heal = (Boss1.get_level() * 2) * 1.5

        player_name = font.render(Knight1.get_name(), 1, (10, 10, 10))
        player_pos = player_name.get_rect(centerx=200, centery=350)
        img_player = pygame.image.load("img/player_img.jpg")
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
            if Atk_Button.is_clicked(event):
                if boss_choice == "Defend":
                    screen.blit(font.render(f"{Knight1.get_name()} attacks {Boss1.get_name()} for {Knight1.get_attack() - Boss1.get_defense()} damage", 1, (255, 10, 10)), (200, 600))
                    screen.blit(font.render(f"{Boss1.get_name()} defends and blocks {(Knight1.get_attack() - Boss1.get_defense()) / 2} damage", 1, (0, 0, 255)), (200, 630))
                    Boss1.set_hp(Boss1.get_hp() - ((Knight1.get_attack() - Boss1.get_defense()) / 2))
                elif boss_choice == "Attack":
                    screen.blit(font.render(f"{Knight1.get_name()} attacks {Boss1.get_name()} for {Knight1.get_attack() - Boss1.get_defense()} damage", 1, (255, 10, 10)), (200, 600))
                    screen.blit(font.render(f"{Boss1.get_name()} attacks {Knight1.get_name()} for {Boss1.get_attack() - Knight1.get_defense()} damage", 1, (255, 0, 0)), (200, 630))
                    Knight1.set_hp(Knight1.get_hp() - (Boss1.get_attack() - Knight1.get_defense()))
                    Boss1.set_hp(Boss1.get_hp() - (Knight1.get_attack() - Boss1.get_defense()))
                else:
                    screen.blit(font.render(f"{Knight1.get_name()} attacks {Boss1.get_name()} for {Knight1.get_attack() - Boss1.get_defense()} damage", 1, (255, 10, 10)), (200, 600))
                    if Boss1.get_hp() == Boss1.get_max_hp():
                        screen.blit(font.render(f"{Boss1.get_name()} is already at max HP!", 1, (255, 0, 255)), (200, 660))
                        Boss1.set_hp(Boss1.get_hp() - (Knight1.get_attack() - Boss1.get_defense()))
                    elif Boss1.get_hp() + boss_heal > Boss1.get_max_hp():
                        Boss1.set_hp(Boss1.get_max_hp())
                        screen.blit(font.render(f"{Boss1.get_name()} sleeps but is almost at max HP!"
                                                f"Only healed for {(Boss1.get_hp() + boss_heal) - Boss1.get_max_hp() }", 1, (255, 0, 255)), (200, 660))
                        Boss1.set_hp(Boss1.get_hp() - (Knight1.get_attack() - Boss1.get_defense()))
                    else:
                        Boss1.set_hp(Boss1.get_hp() + boss_heal)
                        screen.blit(font.render(f"{Boss1.get_name()} sleeps and heals for {boss_heal} HP", 1, (255, 0, 255)), (200, 660))
                        Boss1.set_hp(Boss1.get_hp() - (Knight1.get_attack() - Boss1.get_defense()))

            if Def_Button.is_clicked(event):
                if boss_choice == "Defend":
                    screen.blit(font.render(f"{Knight1.get_name()} and {Boss1.get_name()} both defend", 1, (0, 0, 255)), (200, 600))
                elif boss_choice == "Sleep":
                    screen.blit(font.render(f"{Knight1.get_name()} defends but there is no damage to block", 1, (0, 0, 255)), (200, 600))
                    screen.blit(font.render(f"{Boss1.get_name()} is sleeping", 1, (0, 0, 255)), (200, 630))
                    boss_heal = (Boss1.get_level() * 2) * 1.5
                    if Boss1.get_hp() == Boss1.get_max_hp():
                        screen.blit(font.render(f"{Boss1.get_name()} is already at max HP!", 1, (255, 0, 255)), (200, 660))
                    elif Boss1.get_hp() + boss_heal > Boss1.get_max_hp():
                        Boss1.set_hp(Boss1.get_max_hp())
                        screen.blit(font.render(f"{Boss1.get_name()} sleeps but is almost at max HP!"
                                                f"Only healed for {(Boss1.get_hp() + boss_heal) - Boss1.get_max_hp() }", 1, (255, 0, 255)), (200, 660))
                    else:
                        Boss1.set_hp(Boss1.get_hp() + boss_heal)
                        screen.blit(font.render(f"{Boss1.get_name()} sleeps and heals for {boss_heal} HP", 1, (255, 0, 255)), (200, 660))

                else:
                    screen.blit(font.render(f"{Knight1.get_name()} defends and blocks {(Boss1.get_attack() - Knight1.get_defense()) / 2} damage", 1, (0, 0, 255)), (200, 600))
                    screen.blit(font.render(f"{Boss1.get_name()} attacks {Knight1.get_name()} for {(Boss1.get_attack() - Knight1.get_defense())} damage", 1, (255, 0, 0)), (200, 630))
                    Knight1.set_hp(Knight1.get_hp() - ((Boss1.get_attack() - Knight1.get_defense()) / 2))

            if Sleep_Button.is_clicked(event):
                if Knight1.get_hp() == Knight1.get_max_hp():
                    screen.blit(font.render(f"{Knight1.get_name()} is already at max HP!", 1, (255, 0, 255)), (200, 600))
                    print("Defendddding")
                elif Knight1.get_hp() + player_heal > Knight1.get_max_hp():
                    Knight1.set_hp(Knight1.get_max_hp())
                    screen.blit(font.render(f"{Knight1.get_name()} sleeps but is almost at max HP!"
                                            f"Only healed for {(Knight1.get_hp() + player_heal) - Knight1.get_max_hp()}", 1, (255, 0, 255)), (200, 600))
                else:
                    Knight1.set_hp(Knight1.get_hp() + player_heal)
                if boss_choice == "Defend":
                    screen.blit(font.render(f"{Boss1.get_name()} defends but there is no damage to block", 1, (0, 0, 255)), (200, 660))
                elif boss_choice == "Attack":
                    screen.blit(font.render(f"{Boss1.get_name()} attacks {Knight1.get_name()} for {Boss1.get_attack() - Knight1.get_defense()} damage", 1, (255, 0, 0)), (200, 660))
                    Knight1.set_hp(Knight1.get_hp() - (Boss1.get_attack() - Knight1.get_defense()))
                else:
                    if Boss1.get_hp() == Boss1.get_max_hp():
                        screen.blit(font.render(f"{Boss1.get_name()} is already at max HP!", 1, (255, 0, 255)),
                                    (200, 660))
                    elif Boss1.get_hp() + boss_heal > Boss1.get_max_hp():
                        Boss1.set_hp(Boss1.get_max_hp())
                        screen.blit(font.render(f"{Boss1.get_name()} sleeps but is almost at max HP!"
                                                f"Only healed for {(Boss1.get_hp() + boss_heal) - Boss1.get_max_hp()}",
                                                1, (255, 0, 255)), (200, 660))
                    else:
                        Boss1.set_hp(Boss1.get_hp() + boss_heal)
                        screen.blit(
                            font.render(f"{Boss1.get_name()} sleeps and heals for {boss_heal} HP", 1, (255, 0, 255)),
                            (200, 660))

            pygame.display.flip()

        time.sleep(0.75)
        screen.fill((230, 230, 230))
        screen.blit(font.render(f"Floor {Floor} Turn {Turn}", 1, (10, 10, 10)), (500, 40))

        screen.blit(boss_name, boss_pos)
        screen.blit(img_enemy, (900, 100))
        Boss1.draw_hp_bar(screen, 900, 300, 200, 25)
        screen.blit(font.render(f"HP: {max(int(Boss1.get_hp()), 0)}", 1, (10, 10, 10)), (930, 300))
        screen.blit(font.render(f"Stats", 1, (10, 10, 10)), (975, 400))
        screen.blit(font.render(f"{int(Boss1.get_attack())} Attack", 1, (170, 0, 0)), (940, 430))
        screen.blit(font.render(f"{int(Boss1.get_defense())} Defense", 1, (0, 0, 170)), (940, 460))
        screen.blit(font.render(f"Level {Boss1.get_level()}", 1, (170, 0, 170)), (940, 490))

        screen.blit(player_name, player_pos)
        Knight1.draw_hp_bar(screen, 100, 300, 200, 25)
        screen.blit(font.render(f"HP: {max(int(Knight1.get_hp()), 0)}", 1, (10, 10, 10)), (130, 300))
        screen.blit(font.render(f"XP: {XP_check2} /// {Player_XP_Thr}", 1, (0, 255, 0)), (100, 75))
        screen.blit(font.render(f"Stats", 1, (10, 10, 10)), (175, 400))
        screen.blit(font.render(f"{int(Knight1.get_attack())} Attack", 1, (170, 0, 0)), (140, 430))
        screen.blit(font.render(f"{int(Knight1.get_defense())} Defense", 1, (0, 0, 170)), (140, 460))
        screen.blit(font.render(f"Level {Knight1.get_level()}", 1, (170, 0, 170)), (140, 490))
        screen.blit(img_player, (100, 100))

        Atk_Button.draw(screen)
        Def_Button.draw(screen)
        Sleep_Button.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)

        if Boss1.get_hp() <= 0:
            screen.blit(font.render(f"{Knight1.get_name()} has defeated {Boss1.get_name()} !", 1, (0, 255, 0)), (200, 690))
            screen.blit(font.render(f"Gained {int((Boss1.get_xp() * Scale))} XP!", 1, (0, 255, 0)), (200, 720))
            Knight1.set_xp(int(Knight1.get_xp() + (Boss1.get_xp() * Scale)))
            Boss1.kill()
            if Floor > 5:
                Rarity_Choice = random.choices(misc2.rarity_tiers,
                                           weights=[0.3, 0.2, 0.1, 0.04, 0.04, 0.03, 0.03, 0.03,
                                                    0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                                                    0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                                                    0.01, 0.01, 0.01, 0.01, 0.01], k=1)
                Scale = misc2.rarity_scale[Rarity_Choice[0][5:-4]]
                Boss1.set_name(f"{Rarity_Choice[0]} {random.choice(misc2.enemies)}")
            else:
                Rarity_Choice = misc2.rarity_tiers[0]
                Scale = 1
                Boss1.set_name(f"{Rarity_Choice} {random.choice(misc2.enemies)}")
            boss_index = misc2.enemies.index(Boss1.get_name())
            if os.path.exists(misc2.enemies_png[boss_index]):
                img_enemy = pygame.image.load(misc2.enemies_png[boss_index])
            else:
                img_enemy = pygame.image.load("img/goblin_text.jpg")
            Boss1.set_hp(int(Boss1.get_hp() * Scale))
            Boss1.set_attack(int(Boss1.get_attack() * Scale))
            Boss1.set_defense(int(Boss1.get_defense() * Scale))
            Kill_Count += 1
            Floor += 1
            Turn = 0
        pygame.display.flip()



if __name__ == "__main__": main()
