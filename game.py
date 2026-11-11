from save_load import delete_save, load_game, save_game  # type: ignore
from ui import clear, input_type, type_print  # type: ignore
from world import choose_a_path  # type: ignore

type_print("\n\nWelcome to my text based Adventure Game!")
type_print("\n\nI hope you enjoy!\n\n")
    

def get_name():
    player_name = input_type("What would you like to be called Adventurer? ").strip()
    if len(player_name) < 4:
        type_print("Name must be atleast 4 characters :)")
        clear()
        return get_name()
    print("\n")
    type_print("Ah " + player_name + ", What an excellent name.")
    return player_name


def play_beginning():
    print("\n")
    type_print("Choose your difficulty.")
    difficulty = input_type("Enter one. Easy, Medium, Or Hard? ").lower().strip()
    if difficulty == "medium":
        type_print("Indeed the path you chosen is a simple one.")
        health = 150
        damage = 7
    elif difficulty == "easy":
        type_print("\nIndeed the path you have chosen is a forgiving one.")
        health = 200
        damage = 10
    elif difficulty == "hard":
        type_print("Indeed the path you have chosen is a hard one.")
        health = 75
        damage = 5
    else:
        clear()
        type_print("Please enter a proper difficulty.")
        return play_beginning()
    input_type("\nPress ENTER to continue")
    clear()
    return health, damage


def start_game():
    saved_player = load_game()
    if saved_player is not None:
        type_print("A save file has been found!")
        choice = input_type("A. Continue, B. New Game ").upper().strip()
        if choice == "A":
            clear()
            type_print(f"Welcome back, {saved_player['name']}")
            return choose_a_path(saved_player)
        if choice == "B":
            delete_save()
            clear()
            type_print("Creating a new game...")
            input_type("Press enter to continue")
            clear()
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
