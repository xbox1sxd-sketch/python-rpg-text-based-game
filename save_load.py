import json
import os

SAVE_FILE = "savegame.json"

def save_game(player):
    with open(SAVE_FILE, "w") as f:
        json.dump(player, f)
        

def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return None

def delete_save():
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)