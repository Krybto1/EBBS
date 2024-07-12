import random
import time
import misc
from boss import Boss
from boss import Knight

Turn = 0
Floor = 1
CharName = input("Enter your character name: ")
Boss1 = Boss(f"{misc.rarity_tiers[0]} {'Goblin'}", 75, 13, 7, 1)
Knight1 = Knight(CharName, 150, 15, 10, 1, 25)

Base_Boss_HP = Boss1.get_hp()
Base_Boss_ATK = Boss1.get_attack()
Base_Boss_DEF = Boss1.get_defense()
Base_Boss_LVL = Boss1.get_level()
Base_Knight_HP = Knight1.get_hp()
Base_Knight_ATK = Knight1.get_attack()
Base_Knight_DEF = Knight1.get_defense()
Base_Knight_LVL = Knight1.get_level()
Kill_Count = 0
Scale = 1
Boss_Choices = "Attack", "Defend", "Sleep"

while Knight1.get_hp() >= 0:
    Turn += 1
    Player_XP_Thr = int((100 * Knight1.get_level()) ** 1.05)
    XP_check = Knight1.get_xp()
    while XP_check >= Player_XP_Thr:
        Knight1.set_xp(XP_check - Player_XP_Thr)
        Knight1.level_up()
        XP_check = Knight1.get_xp()

    XP_check2 = Knight1.get_xp()
    Player_XP_Thr = int((100 * Knight1.get_level()) ** 1.05)
    time.sleep(0.4)

    print(f"{'':>75}Floor {Floor} Turn {Turn} \n{'Character':<15}{misc.GREEN}{'HP':<15}{misc.RED}{'Attack':<15}"
          f"{misc.BLUE}{'Defense':<15}{misc.MAGENTA}{'Level':<15}{misc.RESET}{'':>25}{'Boss':30}"
          f" {misc.GREEN}{'HP':<15}{misc.RED}{'Attack':<15}{misc.BLUE}{'Defense':<15}{misc.MAGENTA}{'Level':<15}{misc.RESET}")
    print(
        f"{Knight1.get_name():<15}{max(Knight1.get_hp(), 0):<15}{Knight1.get_attack():<15}{Knight1.get_defense():<15}{Knight1.get_level():<15}"
        f"{'':>25}{Boss1.get_name():<40}{max(Boss1.get_hp(), 0):<15}{Boss1.get_attack():<15}{Boss1.get_defense():<15}{Boss1.get_level():<15}")
    print(f"{misc.GREEN}XP: {XP_check2} /// {Player_XP_Thr:<15}{misc.RESET}")

    time.sleep(0.4)

    boss_choice = random.choice(Boss_Choices)
    choice_att_def = input(
        f"\n{'':<58}What do you want to do? {misc.RED}Attack{misc.RESET}, {misc.BLUE}Defend{misc.RESET} or {misc.MAGENTA}Sleep?{misc.RESET}: ")

    time.sleep(0.4)

    if choice_att_def.lower() in ["a", "atk", "attack"]:
        print(
            f"{'':<58}{Knight1.get_name()} {misc.RED}attacks{misc.RESET} {Boss1.get_name()} for {Knight1.get_attack() - Boss1.get_defense()} damage")
        if boss_choice == "Defend":
            print(
                f"{'':<58}{Boss1.get_name()} {misc.BLUE}defends{misc.RESET} and {misc.CYAN}blocks{misc.RESET} {(Knight1.get_attack() - Boss1.get_defense()) / 2} damage")
            Boss1.set_hp(Boss1.get_hp() - ((Knight1.get_attack() - Boss1.get_defense()) / 2))
        else:
            Boss1.set_hp(Boss1.get_hp() - (Knight1.get_attack() - Boss1.get_defense()))

    elif choice_att_def.lower() in ["d", "def", "defend"]:
        print(
            f"{'':<58}{Knight1.get_name()} {misc.BLUE}defends{misc.RESET} and {misc.CYAN}blocks{misc.RESET} {Boss1.get_attack() / 2} damage")
        Knight1.set_hp(Knight1.get_hp() - ((Boss1.get_attack() - Knight1.get_defense()) / 2))

    else:
        heal = (Knight1.get_level() * 5) * 1.5
        Knight1.set_hp(Knight1.get_hp() + heal)
        print(f"{'':<58}{Knight1.get_name()} {misc.MAGENTA}sleeps{misc.RESET} and regains {heal} HP")

    time.sleep(0.4)

    if boss_choice == "Attack":
        print(
            f"{'':<58}{Boss1.get_name()} {misc.RED}attacks{misc.RESET} {Knight1.get_name()} for {Boss1.get_attack() - Knight1.get_defense()} damage")
        Knight1.set_hp(Knight1.get_hp() - (Boss1.get_attack() - Knight1.get_defense()))

    if boss_choice == "Sleep":
        heal = (Boss1.get_level() * 2) * 1.5
        Boss1.set_hp(Boss1.get_hp() + heal)
        print(f"{'':<58}{Boss1.get_name()} {misc.MAGENTA}sleeps{misc.RESET} and regains {heal} HP")

    time.sleep(0.4)

    print("\n" * 3)
    if Boss1.get_hp() <= 0:
        print(f"{'':<58}{Knight1.get_name()} has {misc.BRIGHT_BLUE}defeated{misc.RESET} {Boss1.get_name()} !")

        print(f"Gained {int((Boss1.get_xp() * Scale))} XP! ")
        Knight1.set_xp(int(Knight1.get_xp() + (Boss1.get_xp() * Scale)))
        Boss1.kill()
        Rarity_Choice = random.choices(misc.rarity_tiers,
                                       weights=[0.3, 0.2, 0.1, 0.04, 0.04, 0.03, 0.03, 0.03,
                                                0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                                                0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                                                0.01, 0.01, 0.01, 0.01, 0.01], k=1)
        Scale = misc.rarity_scale[Rarity_Choice[0][5:-4]]
        Boss1.set_name(f"{Rarity_Choice[0]} {random.choice(misc.enemies)}")
        Boss1.set_hp(int((Base_Boss_HP + (30 * Boss1.get_level())) * Scale))
        Boss1.set_attack(int((Base_Boss_ATK + (3 * Boss1.get_level())) * Scale))
        Boss1.set_defense(int((Base_Boss_DEF + (1 * Boss1.get_level())) * Scale))
        Kill_Count += 1
        Floor += 1
        Turn = 0

    elif Knight1.get_hp() <= 0:
        print(f"{'':<58}{Boss1.get_name()} has {misc.BRIGHT_RED}defeated{misc.RESET} {Knight1.get_name()}")
        break

    time.sleep(0.4)
    print("\n" * 3)

print(f"{misc.BRIGHT_RED} Game Over {misc.RESET} \nYou have defeated {Kill_Count} bosses")

# TODO: Save Game Progress
