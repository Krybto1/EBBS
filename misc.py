RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

RESET = "\033[0m"

BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

enemies = [
    "Goblin Grunt",
    "Goblin Shaman",
    "Goblin Berserker",
    "Spectral Wraith",
    "Phantom Lurker",
    "Haunted Apparition",
    "Cursed Spirit",
    "Undead Warrior",
    "Zombie Horde",
    "Vampire Lord",
    "Werewolf Pack",
    "Skeleton Knight",
    "Shadow Fiend",
    "Dark Sorcerer",
    "Eldritch Abomination",
    "Ancient One",
    "Cosmic Horror",
    "Void Reaper",
    "Elder God",
    "Cthulhu",
    "Nyarlathotep",
    "Shub-Niggurath",
    "Azathoth",
    "Yog-Sothoth",
    "Deep One",
    "Star Spawn",
    "Lurker at the Threshold",
    "Nightgaunt",
    "Dagon",
    "Fire Elemental",
    "Ice Elemental",
    "Earth Elemental",
    "Storm Elemental",
    "Chaos Beast",
    "Demonic Overlord",
    "Hellfire Imp",
    "Abyssal Devourer",
    "Netherworld Wraith"
]

rarity_tiers = [
    f"{GREEN}Common{RESET}",
    f"{GREEN}Uncommon{RESET}",
    f"{GREEN}Rare{RESET}",
    f"{GREEN}Epic{RESET}",
    f"{YELLOW}Legendary{RESET}",
    f"{YELLOW}Mythic{RESET}",
    f"{YELLOW}Exotic{RESET}",
    f"{YELLOW}Ancient{RESET}",
    f"{YELLOW}Fabled{RESET}",
    f"{RED}Heroic{RESET}",
    f"{RED}Masterwork{RESET}",
    f"{RED}Miraculous{RESET}",
    f"{RED}Mystical{RESET}",
    f"{RED}Obscure{RESET}",
    f"{RED}Phantasmal{RESET}",
    f"{RED}Relic{RESET}",
    f"{CYAN}Sacred{RESET}",
    f"{CYAN}Secret{RESET}",
    f"{CYAN}Shiny{RESET}",
    f"{CYAN}Supreme{RESET}",
    f"{CYAN}Transcendent{RESET}",
    f"{CYAN}Unparalleled{RESET}",
    f"{MAGENTA}Untouchable{RESET}",
    f"{MAGENTA}Zenith{RESET}",
    f"{MAGENTA}Supreme Legendary{RESET}",
    f"{MAGENTA}Divine{RESET}",
    f"{MAGENTA}Celestial{RESET}",
    f"{MAGENTA}Cosmic{RESET}"
]

rarity_scale = {
    "Common": 1,
    "Uncommon": 1.03,
    "Rare": 1.07,
    "Epic": 1.1,
    "Legendary": 1.14,
    "Mythic": 1.17,
    "Exotic": 1.23,
    "Ancient": 1.26,
    "Fabled": 1.3,
    "Heroic": 1.35,
    "Masterwork": 1.42,
    "Miraculous": 1.49,
    "Mystical": 1.55,
    "Obscure": 1.6,
    "Phantasmal": 1.68,
    "Relic": 1.73,
    "Sacred": 1.76,
    "Secret": 1.8,
    "Shiny": 1.87,
    "Supreme": 1.95,
    "Transcendent": 2.07,
    "Unparalleled": 2.16,
    "Untouchable": 2.21,
    "Zenith": 2.25,
    "Supreme Legendary": 2.3,
    "Divine": 2.35,
    "Celestial": 2.4,
    "Cosmic": 2.5
}