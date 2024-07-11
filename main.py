from boss import Boss
from boss import Knight

Turn = 0
Boss1 = Boss("Goblin", 100, 5, 5, 1)
Knight1 = Knight("Arthur", 100, 10, 3, 1)
print(f"{'':>80}Turn {Turn} \n{'Boss':<15}{'HP':<15}{'Attack':<15}{'Defense':<15}{'Level':<15}{'':>25}{'Boss':<15}"
      f"{'HP':<15}{'Attack':<15}{'Defense':<15}{'Level':<15}")
print(f"{Knight1.get_name():<15}{Knight1.get_hp():<15}{Knight1.get_attack():<15}{Knight1.get_defense():<15}{Knight1.get_level():<15}"
      f"{'':>25}{Boss1.get_name():<15}{Boss1.get_hp():<15}{Boss1.get_attack():<15}{Boss1.get_defense():<15}{Boss1.get_level():<15}")



