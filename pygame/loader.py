import json

def load(file):
    with open(file) as f:
        return json.load(f)["shop_items"]

def get_item_by_name(items, name):
    for item in items:
        if item["name"] == name:
            return item
    return None


def load_skills(file_path):
    with open(file_path) as file:
        return json.load(file)


def get_skill_by_id(skills, id_):
    for skill in skills:
        if skill['id'] == id_:
            return skill


def get_skill_cost(skills, id_):
    return get_skill_by_id(skills, id_)['skill_cost']


def skill_dependencies(skills, id_):
    return get_skill_by_id(skills, id_)['dependencies']


def set_skill_unlocked(skills, id_):
    get_skill_by_id(skills, id_)['is_unlocked'] = True


def buy_skill(skills, id_, skill_points):
    dep_unlocked = []
    if skill_points < get_skill_cost(skills, id_):
        return False, skill_points  # Skill nicht gekauft, Punkte bleiben gleich

    for dependency_id in skill_dependencies(skills, id_):
        if not get_skill_by_id(skills, dependency_id)['is_unlocked']:
            dep_unlocked.append(False)
        else:
            dep_unlocked.append(True)

    if False in dep_unlocked:
        return False, skill_points  # Skill nicht gekauft, Punkte bleiben gleich

    # Skill kaufen
    skill_points -= get_skill_cost(skills, id_)
    set_skill_unlocked(skills, id_)
    return True, skill_points  # Skill gekauft, aktualisierte Punkte zurückgeben




if __name__ == "__main__":
    items = load("items.json")
    print(get_item_by_name(items, "Stick"))