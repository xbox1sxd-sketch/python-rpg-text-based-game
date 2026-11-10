import random

from ui import clear, input_type, type_print  # type: ignore


def show_inventory(player):
    type_print("\n --- INVENTORY ---")
    if player["inventory"] == []:
        type_print("Your pack is empty.")
    else:
        for item in player["inventory"]:
            type_print(" -" + item)
    type_print(f"\n Gold: {player['gold']}")
    type_print(f"Health: {player['health']}/{player['max_health']}")
    type_print(f"Damage: {player['damage']}")
    input_type("Press Enter to continue")
    clear()

def use_potion(player):
    if "Health Potion" not in player["inventory"]:
        type_print("You dig around in your pack... No potions. :(")
        return False
    if player["health"] >= player["max_health"]:
        type_print("You're already at full health.")
        return False
    player["inventory"].remove("Health Potion")
    old_health = player["health"]
    player["health"] += 50
    if player["health"] > player["max_health"]:  # noqa: PLR1730
        player["health"] = player["max_health"]
    type_print(f"You heal {player['health'] - old_health} health")
    type_print(f"Health: {player['health']}/{player['max_health']}")
    return True    
    
def pickup(player, item):
    player["inventory"].append(item)
    type_print("you got a " + item + "!")
    
def silver_scythe(player):
    if "Silver Scythe" in player["inventory"]:
        return False
    player["damage"] += 2
    pickup(player, "Silver Scythe")
    type_print(f"Your damage now is {player['damage']}")
    return True

def open_chest(player):
    type_print("you open the chest")    
    gold_found = random.randint(5, 20)
    player["gold"] += gold_found
    type_print(f"You find {gold_found} gold!")
    roll = random.randint(1, 100)
    if roll <= 55:
        pickup(player, "Health Potion")
    elif roll <= 80:
        if silver_scythe(player) == False:
            gold_found = random.randint(10, 25)
            player["gold"] += gold_found
            type_print(f"you leave the scythe and grab {gold_found} gold instead ")        
    elif roll <= 90:
        if silver_scythe(player) == False:
             gold_found = random.randint(10, 25)
             player["gold"] += gold_found
             type_print(f"You leave the scythe and grab {gold_found} gold instead")
        pickup(player, "Health Potion")
        type_print("WOW")
    else:
        type_print("... and nothing else. Somebody else got here first!")