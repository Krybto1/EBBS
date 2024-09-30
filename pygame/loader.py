import json

def load(file):
    with open(file) as f:
        return json.load(f)["shop_items"]

def get_item_by_name(items, name):
    for item in items:
        if item["name"] == name:
            return item
    return None


if __name__ == "__main__":
    items = load("items.json")
    print(get_item_by_name(items, "Iron Sword"))