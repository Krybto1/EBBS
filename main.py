import random
import colors
from boss import Boss
from boss import Knight

Turn = 0
CharName = input("Enter your character name: ")
Boss1 = Boss("Goblin", 100, 5, 5, 1)
Knight1 = Knight(CharName, 100, 15, 10, 1, 0)

Base_Boss_HP = Boss1.get_hp()
Base_Boss_ATK = Boss1.get_attack()
Base_Boss_DEF = Boss1.get_defense()
Base_Boss_LVL = Boss1.get_level()
Base_Knight_HP = Knight1.get_hp()
Base_Knight_ATK = Knight1.get_attack()
Base_Knight_DEF = Knight1.get_defense()
Base_Knight_LVL = Knight1.get_level()
Player_XP_Thr = (100 * Knight1.get_level()) * 1.5
Kill_Count = 0
Boss_Choices = "Attack", "Defend", "Sleep"

while Knight1.get_hp() >= 0: #and Boss1.get_hp() >= 0:
    Turn += 1
    XP_check = Knight1.get_xp()
    print(f"{'':>80}Turn {Turn} \n{'Character':<15}{'HP':<15}{'Attack':<15}{'Defense':<15}{'Level':<15}{'':>25}{'Boss':<15}"
          f"{'HP':<15}{'Attack':<15}{'Defense':<15}{'Level':<15}")
    print(f"{Knight1.get_name():<15}{max(Knight1.get_hp(), 0):<15}{Knight1.get_attack():<15}{Knight1.get_defense():<15}{Knight1.get_level():<15}"
          f"{'':>25}{Boss1.get_name():<25}{max(Boss1.get_hp(), 0):<15}{Boss1.get_attack():<15}{Boss1.get_defense():<15}{Boss1.get_level():<15}")
    print(f"{colors.GREEN}XP: {Knight1.get_xp()} /// {Player_XP_Thr:<15}{colors.RESET}")

    boss_choice = random.choice(Boss_Choices)
    choice_att_def = input(f"\n{'':<68}What do you want to do? Attack or Defend: ")

    if choice_att_def.lower() in ["a", "atk", "attack"]:
        print(f"{'':<68}{Knight1.get_name()} attacks {Boss1.get_name()}")
        if boss_choice == "Defend":
            print(f"{'':<68}{Boss1.get_name()} defends")
            Boss1.set_hp(Boss1.get_hp() - ((Knight1.get_attack() - Boss1.get_defense()) / 2))
        else:
            Boss1.set_hp(Boss1.get_hp() - (Knight1.get_attack() - Boss1.get_defense()))

    elif choice_att_def == "Defend" or choice_att_def == "defend" or choice_att_def == "D" or choice_att_def == "d":
        print(f"{'':<68}{Knight1.get_name()} defends")
        Boss1.set_attack(Boss1.get_attack() / 2)

    else:
        heal = (Knight1.get_level() * 5) * 1.5
        Knight1.set_hp(Knight1.get_hp() + heal)
        print(f"{'':<68}{Knight1.get_name()} sleeps and regains {heal} HP")

    if boss_choice == "Attack":
        print(f"{'':<68}{Boss1.get_name()} attacks {Knight1.get_name()}")
        Knight1.set_hp(Knight1.get_hp() - Boss1.get_attack())

    elif boss_choice == "Sleep":
        heal = (Boss1.get_level() * 3) * 1.5
        Boss1.set_hp(Boss1.get_hp() + heal)
        print(f"{'':<68}{Boss1.get_name()} sleeps and regains {heal} HP")
        continue

    if Boss1.get_hp() <= 0:
        print(f"{'':<68}{Knight1.get_name()} has defeated {Boss1.get_name()}")
        Boss.kill(self=Boss1)
        Knight1.set_xp(Knight1.get_xp() + Boss1.kill())
        Boss1.set_name(random.choice(colors.enemies))

    elif Knight1.get_hp() <= 0:
        print(f"{'':<68}{Boss1.get_name()} has defeated {Knight1.get_name()}")
        break

    if XP_check >= Player_XP_Thr:
        Knight1.set_xp(XP_check - Player_XP_Thr)
        Knight1.level += 1
        Knight1.hp = Base_Knight_HP + (75 * Knight1.get_level())
        Knight1.atk += 7
        Knight1.defense += 4



print("game over")