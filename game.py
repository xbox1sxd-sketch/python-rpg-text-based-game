import os

print("Hi, welcome to my text based Adventure Game!")
print("Hope you have fun!\n\n")


def get_name():
    player_name = input("What would you like to be called Adventurer? ")
    print("\n")
    print("Ah " + player_name + " What an excellent name.")

    return player_name

def play_beginning():
    print("\n")
    print("Choose your difficulty.")
    difficulty = input("Enter one. Easy, Medium, Or Hard ").lower()
    if difficulty == "medium":
        print("Indeed the path you chosen is a simple one.")
        health = 150
        damage = 3
    elif difficulty == "easy":
        print("\nIndeed the path you have chosen is a forgiving one.")
        health = 200
        damage = 5
    elif difficulty == "hard":
        print("Indeed the path you have chosen is a hard one.")
        health = 75
        damage = 1
    else:
        print("Please enter a proper difficulty.")
        return play_beginning()
    input("\nPress ENTER to continue")
    os.system('cls')
    return health, damage

player_name = get_name()
player_health, player_damage = play_beginning()
print("\nWelcome, " + player_name + "!")
print(f"Your starting health is {player_health} and your starting damage is {player_damage}")