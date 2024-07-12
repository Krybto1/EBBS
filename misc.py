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
    "Uncommon": 1.1,
    "Rare": 1.15,
    "Epic": 1.2,
    "Legendary": 1.3,
    "Mythic": 1.4,
    "Exotic": 1.5,
    "Ancient": 1.6,
    "Fabled": 1.7,
    "Heroic": 1.8,
    "Masterwork": 2,
    "Miraculous": 2.1,
    "Mystical": 2.2,
    "Obscure": 2.3,
    "Phantasmal": 2.4,
    "Relic": 2.5,
    "Sacred": 2.6,
    "Secret": 2.7,
    "Shiny": 2.8,
    "Supreme": 2.9,
    "Transcendent": 3,
    "Unparalleled": 3.2,
    "Untouchable": 3.4,
    "Zenith": 3.6,
    "Supreme Legendary": 3.8,
    "Divine": 4,
    "Celestial": 4.5,
    "Cosmic": 5
}