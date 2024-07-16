import pygame
from boss import Boss
from boss import Knight
import misc2
import random


CharName = input("Enter your character name: ")
Knight1 = Knight(CharName, 100, 15, 10, 1, 0)
Boss1 = Boss(f"{misc2.rarity_tiers[0]} {'Goblin'}", 75, 13, 5, 1)
#Rarity_Choice = random.choices(misc2.rarity_tiers,
#                               weights=[0.3, 0.2, 0.1, 0.04, 0.04, 0.03, 0.03, 0.03,
#                                        0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
#                                        0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
#                                        0.01, 0.01, 0.01, 0.01, 0.01], k=1)
#Scale = misc2.rarity_scale[Rarity_Choice[0][5:-4]]
#Boss1.set_name(f"{Rarity_Choice[0]} {random.choice(misc2.enemies)}")


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
    Boss_Choices = "Attack", "Defend", "Sleep"
    pygame.init()
    font_loader = "C:/Windows/Fonts/Calibri.ttf"
    font = pygame.font.Font(font_loader, 27)
    button_surface = pygame.Surface((100, 50))
    button_attack_text = font.render("Attack", True, (255, 255, 255))
    button_attack_text_rect = button_attack_text.get_rect(
        center=(button_surface.get_width() / 2, button_surface.get_height() / 2))
    button_rect = pygame.Rect(125, 125, 150, 50)
    button_surface.fill((100, 10, 10))

    boss_name = font.render(Boss1.get_name(), 1, (10, 10, 10))
    boss_pos = boss_name.get_rect(centerx=1000, centery=350)

    player_name = font.render(Knight1.get_name(), 1, (10, 10, 10))
    player_pos = player_name.get_rect(centerx=200, centery=350)

    img_enemy = pygame.image.load("img/goblin_test.jpg")
    img_enemy = pygame.transform.scale(img_enemy, (200, 200))

    img_player = pygame.image.load("img/player_img.jpg")
    img_player = pygame.transform.scale(img_player, (200, 200))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((230, 230, 230))
        screen.blit(boss_name, boss_pos)
        screen.blit(player_name, player_pos)
        screen.blit(img_enemy, (900, 100))
        screen.blit(img_player, (100, 100))

        screen.blit(button_surface, (550, 200))
        button_surface.blit(button_attack_text, button_attack_text_rect)
        pygame.display.flip()
        dt = clock.tick(60)

    if Boss1.get_hp() <= 0:
        print(f"{'':<58}{Knight1.get_name()} has {misc2.BRIGHT_BLUE}defeated{misc2.RESET} {Boss1.get_name()} !")
        print(f"Gained {int((Boss1.get_xp() * Scale))} XP! ")
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
        Boss1.set_hp(int(Boss1.get_hp() * Scale))
        Boss1.set_attack(int(Boss1.get_attack() * Scale))
        Boss1.set_defense(int(Boss1.get_defense() * Scale))
        Kill_Count += 1
        Floor += 1
        Turn = 0


if __name__ == "__main__": main()
