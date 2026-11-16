from save_load import delete_save, load_game, save_game  # type: ignore
from ui import clear, input_type, pause, type_print  # type: ignore
from world import choose_a_path  # type: ignore

type_print("\n\nWelcome to my text based Adventure Game!")
type_print("\nI hope you enjoy!\n\n")
    
#You choose your name
def get_name():
    while True:
        player_name = input_type("What would you like to be called Adventurer? ").strip()
        if len(player_name) < 4:
            break
        type_print("Name must be atleast 4 characters :)")
        clear()
    print("\n")
    type_print("Ah " + player_name + ", What an excellent name.")
    return player_name

#You choose easy medium or hard
def play_beginning():
    print("\n")
    type_print("Choose your difficulty.")
    while True:
        difficulty = input_type("Enter one. Easy, Medium, Or Hard? ").lower().strip()
        
        if difficulty == "medium":
            type_print("Indeed the path you chosen is a simple one.")
            health, damage = 150, 7
            break
        elif difficulty == "easy":
            type_print("\nIndeed the path you have chosen is a forgiving one.")
            health, damage = 200, 10
            break
        elif difficulty == "hard":
            type_print("Indeed the path you have chosen is a hard one.")
            health, damage = 75, 5
            break
        else:
            type_print("Please ENTER a proper difficulty.")
    pause()
    clear()
    return health, damage

#The starting dictionary that holds everything, also finds if you have a save file or not
def start_game():
    saved_player = load_game()
    if saved_player is not None:
        type_print("A save file has been found!")
        while True:
            choice = input_type("A. Continue, B. New Game ").upper().strip()
            if choice == "A":
                clear()
                type_print(f"Welcome back, {saved_player['name']}")
                return choose_a_path(saved_player)
            if choice == "B":
                delete_save()
                clear()
                type_print("Creating a new game...")
                pause()
                clear()
                break
            type_print("Please choose A or B")
    player_name = get_name()
    player_health, player_damage = play_beginning()
    player = {
    "name": player_name,
    "warden_dead": False,
    "sealed_one_dead": False,
    "whetstone_bought": False,
    "iron_heart_bought": False,
    "dungeon_floor": 0,
    "damage": player_damage,
    "health": player_health,
    "max_health": player_health,
    "inventory": [],
    "gold": 0,
    "armour": 0,
    "arena_wave": 0,
    "witch_dead": False,
    "bandit_leader_dead": False,
    "guardian_dead": False,
    }   
    type_print(f"\nWelcome {player_name}!")
    type_print(f"Your starting health is {player_health} and your starting damage is {player_damage}.")
    save_game(player)
    return choose_a_path(player)

def main():
    while True:
        replay = start_game()
        if replay == False:
            break



if __name__ == "__main__":
    main()
