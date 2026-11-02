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
        return health
    elif difficulty == "easy":
        print("indeed the path you have chosen is a forgiving one.")
        health = 200
        return health
    elif difficulty == "hard":
        print("Indeed the path you have chosen is a hard one.")
        health = 75
        return health
    else:
        print("Please enter a proper difficulty.")
        return play_beginning()

player_name = get_name()
player_health = play_beginning()
print("\n Welcome, " + player_name + " !")
print(f"Your starting health is {player_health} hp")