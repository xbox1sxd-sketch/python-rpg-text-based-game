
import os
import time


def type_print(text, delay = 0.03):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(delay)
    print()
    
def input_type(text, delay = 0.03):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(delay)
    return input()
    
type_print("\n\nHi, welcome to my text based Adventure Game!")
type_print("\n\nHope you have fun!\n\n")
    
def get_name():
    player_name = input_type("What would you like to be called Adventurer? ")
    print("\n")
    type_print("Ah " + player_name + " What an excellent name.")

    return player_name

def play_beginning():
    print("\n")
    type_print("Choose your difficulty.")
    difficulty = input_type("Enter one. Easy, Medium, Or Hard? ").lower()
    if difficulty == "medium":
        type_print("Indeed the path you chosen is a simple one.")
        health = 150
        damage = 3
    elif difficulty == "easy":
        type_print("\nIndeed the path you have chosen is a forgiving one.")
        health = 200
        damage = 5
    elif difficulty == "hard":
        type_print("Indeed the path you have chosen is a hard one.")
        health = 75
        damage = 1
    else:
        os.system('cls')
        type_print("Please enter a proper difficulty.")
        return play_beginning()
    input_type("\nPress ENTER to continue")
    os.system('cls')
    return health, damage

def choose_a_path():
    path = input_type("\nNow, where would you like to go? A: A shimmering city. B: A dark forest. C: Through the swamp. ").upper()
    if path == "A":
        os.system('cls')
        return shimmering_city()
    elif path == "B":
        os.system('cls')
        return dark_forest()
    elif path == "C":
        os.system()
        return swamp
    else:
        os.system('cls')
        type_print("Please choose A, B, or C")
        
        return choose_a_path()
    os.system('cls')

def shimmering_city():
    os.system('cls')
    type_print("You make your way down to the city... unfortunately you somehow get stopped by the guards for not having any ID.")
    guards = input_type("Do you A. Turn back to the crossroads. B: Say you'll turn back and try to sneak past them. C: Fight ").upper()
    if guards == "A":
        os.system('cls')
        return choose_a_path()
    elif guards == "B":
        os.system('cls')
        type_print("Somehow, this managed to work. You are now inside the city.")
    elif guards == "C":
        os.system('cls')
        print("you got instantly obliterated.")
        return play_beginning()
    else:
        type_print("please enter a proper difficulty.")
        return shimmering_city()

def dark_forest():
    type_print("You slowly make your way to the forest... Then the sound of an owl scares the hell out of you. ")
    time.sleep(0.5)
    type_print("You turn back.")
    time.sleep(0.5)
    os.system('cls')
    return choose_a_path()

def swamp():
    path = input_type("you trek your way through the swamp. There you see two things, which do you go to? A.) A Witches hut. B.) A seperate secret enterence to the city.").upper()
    if path == "A":
        witch = input_type("You make your way into the witches hut. Inside you see the witch sleeping. Do you A. Kill her. or B. Wake her up?").upper()
        if witch == "A":
            type_print("You tried to kill her, but failed as she suddenly rolled over. This woke her up. You died.")
            return play_beginning
        elif witch == "B":
            print("You really scared her as shes used to solitude. You died.")
            return play_beginning()
    elif path == "B":
        return shimmering_city()
    else:
        type_print("Please say A, or B")
        return swamp()
    
    



player_name = get_name()
player_health, player_damage = play_beginning()
print("\nWelcome, " + player_name + "!")
print(f"Your starting health is {player_health} and your starting damage is {player_damage}.")
choose_a_path()
