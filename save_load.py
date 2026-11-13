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
            if "armour" not in player:
                player["armour"] = 0
            return player
    return None

def delete_save():
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)