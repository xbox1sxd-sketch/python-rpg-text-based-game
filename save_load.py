import json
import os

SAVE_FILE = "savegame.json"

def save_game(player):
    with open(SAVE_FILE, "w") as f:
        json.dump(player, f)
        

def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            player = json.load(f)
            defaults = {
                "armour": 0,
                "warden_dead": False,
                "sealed_one_dead": False,
                "whetstone_bought": False,
                "iron_heart_bought": False,
                "dungeon_floor": 0,
                "gold": 0,
                "bandit_leader_dead": False,
                "inventory": [],
            }
            for key, value in defaults.items():
                if key not in player:
                    player[key] = value
            return player
                    
    return None

def delete_save():
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)