
import msvcrt
import os
import random
import time


#used ai for type_print function, and for msvcrt
def type_print(text, delay = 0.03):
    for i, letter in enumerate(text):
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\r':
                print(text[i:], end="", flush=True)
                break
        print(letter, end="", flush=True)
        time.sleep(delay)
    print()
    while msvcrt.kbhit():
        key = msvcrt.getch()


def input_type(text, delay=0.03):
    for i, letter in enumerate(text):
        if msvcrt.kbhit():
            key = msvcrt.getch()

            if key == b'\r':
                print(text[i:], end="", flush=True)
                break

        print(letter, end="", flush=True)
        time.sleep(delay)

    return input()


type_print("\n\n Welcome to my text based Adventure Game!")
type_print("\n\n I hope you enjoy!\n\n")
    

def get_name():
    player_name = input_type("What would you like to be called Adventurer? ").strip()
    if len(player_name) < 4:
        type_print("Name must be atleast 4 characters :)")
        os.system('cls')
        return get_name()
    print("\n")
    type_print("Ah " + player_name + " What an excellent name.")
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
        os.system('cls')
        type_print("Please enter a proper difficulty.")
        return play_beginning()
    input_type("\nPress ENTER to continue")
    os.system('cls')
    return health, damage

def choose_a_path(player):
    path = input_type("\nNow, where would you like to go? A: A shimmering city. B: A dark forest. C: Through the swamp. I: Inventory P: Drink a health pot ").upper()
    if path == "A":
        os.system('cls')
        return shimmering_city(player)
    elif path == "B":
        os.system('cls')
        return dark_forest(player)
    elif path == "C":
        os.system('cls')
        return swamp(player)
    elif path == "I":
        os.system('cls')
        show_inventory(player)
        return choose_a_path(player)
    elif path == "P":
        os.system('cls')
        use_potion(player)
        return choose_a_path(player)
    else:
        os.system('cls')
        type_print("Please choose A, B, or C, I, or P")
        
        return choose_a_path(player)


def shimmering_city(player):
    os.system('cls')
    type_print("You make your way down to the city... unfortunately you somehow get stopped by the guard for not having any ID.")
    guards = input_type("Do you A. Turn back to the crossroads. B: Say you'll turn back and try to sneak past them. C: Fight ").upper()
    if guards == "A":
        os.system('cls')
        return choose_a_path(player)
    elif guards == "B":
        os.system('cls')
        type_print("This managed to work. You are now inside the city.")
        return inside_city(player)
    elif guards == "C":
        os.system('cls')
        return combat(player, 30, 5, "guard", "city")
    else:
        type_print("please enter A. B. or C.")
        return shimmering_city(player)

def dark_forest(player):
    encounter = random.randint(1, 10)
    if 1 <= encounter <= 6:
        type_print("A wolf approaches you!")
        return combat(player, 25, 5, "wolf")
    elif 7 <= encounter <= 9:
        type_print("A goblin approaches you!")
        return combat(player, 50, 8, "goblin")
    else:
        type_print("You discover a treasure chest! How rare!")
        open_chest(player)
    return choose_a_path(player)

def swamp(player):
    path = input_type("you trek your way through the swamp. There you see two things, which do you go to? A.) A Witches hut. B.) A seperate secret enterence to the city.").upper()
    if path == "A":
        witch = input_type("You make your way into the witches hut. Inside you see the witch sleeping. Do you A. Kill her. or B. Wake her up?").upper()
        if witch == "A":
            type_print("You tried to kill her, but failed as she suddenly rolled over. This woke her up. You died.")
            input_type("press enter to continue")
            os.system('cls')
            return start_game()
        elif witch == "B":
            type_print("You really scared her as shes used to being alone. You died.")
            input_type("press enter to continue")
            os.system('cls')
            return start_game()
        else:
            type_print("Please type A or B.")
            return swamp(player)
            
    elif path == "B":
        return shimmering_city(player)
    else:
        type_print("Please say A, or B")
        return swamp(player)

def inside_city(player):
    os.system('cls')
    type_print("You now sneak past the gates into the shimmering city")
    type_print("It is beautiful, unlike any city you have ever seen.")
    choice = input_type("What do you do? A.) Look for the blacksmith. B.) Wander around. C. Leave").upper().strip()
    if choice == "A":
        os.system('cls')
        return shop(player)
    elif choice == "B":
        os.system('cls')
        return wander_streets(player)
    elif choice == "C":
        os.system('cls')
        return choose_a_path(player)
    else:
        type_print("please enter A, B, OR C")
        os.system('cls')
        return inside_city(player)

def shop(player):
    os.system('cls')
    type_print(" A exhausted looking blacksmith looks up from this anvil? 'What'll it be' he says")
    type_print(f"You have {player['gold']} gold (earn more from fighting).")
    choice = input_type("A: A health potion (10g). B: A Gold Scythe (+3 damage, 30g) Or C: Leave").upper().strip()
    if choice == "A":
        if player["gold"] >= 10:
            player["gold"] -= 10
            pickup(player, "Health Potion")
            input_type("Press enter to continue")
            return shop(player)
        else:
            type_print("You dont have enough gold.")
            input_type("press enter to continue")
            os.system('cls')
            return shop(player)
    elif choice == "B":
        if "Gold Scythe" in player["inventory"]:
            type_print("You cant buy another")
            input_type("Press enter to continue")
            return shop(player)
        if player["gold"] >= 30:
            player["gold"] -= 30
            player["damage"] += 3
            type_print(f"Congrats! Your damage is now {player['damage']}")
            pickup(player, "Gold Scythe")
            input_type("Press enter to continue")
            return shop(player)
        else:
            type_print("you dont have enough gold :(")
            input_type("Press enter to continue")
            os.system('cls')
            return shop(player)
    elif choice == "C":
        return inside_city(player)
    else:
        type_print("Please choose A, B, or C")
        input_type("Press enter to continue")
        return shop(player)

def wander_streets(player):
    os.system('cls')
    roll = random.randint(1, 10)
    if roll <= 4:
        gold_found = random.randint(10, 30)
        player["gold"] += gold_found
        type_print(f"you spot a wallet on the floor +{gold_found} gold")
        input_type("Press enter to continue")
        return inside_city(player)
    elif roll <= 7:
        type_print("An angry dude thinks you stole his wallet!")
        return combat(player, 40, 10, "angry dude", "city")
    else:
        type_print("Nothing worthwhile here")
        input_type("Press enter to continue")
        return inside_city(player)

def combat(player, enemy_health, enemy_damage, enemy_name, next = "crossroads"):
    type_print(f"You encounter a {enemy_name}.")
    type_print(f"It has {enemy_health} health!")
    while enemy_health > 0 and player["health"] > 0:
        choice = input_type("Would you like to A.) Attack or B.) Flee C.) Use a Potion ").strip().upper()
        if choice == "A":
            enemy_health -= player["damage"]
            type_print(f"you did {player['damage']} damage!")
            type_print(f"It has {enemy_health} health left!")
            damage_dealt = random.randint(enemy_damage - 2, enemy_damage + 2)
            if enemy_health > 0:
                player["health"] -= damage_dealt
                type_print(f"The {enemy_name} did {damage_dealt} damage! You have {player['health']} health left!" )
        elif choice == "B":
            type_print("You scream and run away")
            if next == "city":
                return inside_city(player)
            return choose_a_path(player)
        elif choice == "C":
            if use_potion(player) == False:
                type_print("You fumble in your pack and waste your turn :sob:")
                damage_dealt = random.randint(enemy_damage -2, enemy_damage +2)
                player["health"] -= damage_dealt
                type_print(f"The {enemy_name} did {damage_dealt} damage while you were fooling around! you have {player['health']} health left! ")
        else:
            type_print("Please choose A, B or C")
    if enemy_health <= 0:
        type_print("YOU WON!")
        enemy_drop(player, enemy_name)
        input_type("press enter to continue")
        if next == "city":
            return inside_city(player)
        return choose_a_path(player)
    elif player["health"] <= 0:
        type_print("You lost LOL")
        input_type("Press enter to continue")
        return start_game()
        
def enemy_drop(player, enemy_name):
    roll = random.randint(1, 100)
    if roll <= 30:
        type_print(f"The {enemy_name} was holding something...")
        pickup(player, "Health Potion")
    elif roll <= 60:
        gold_found = random.randint(10, 20)
        player["gold"] += gold_found
        type_print(f"You got {gold_found} gold from that corpse!")

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
    os.system('cls')

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
        silver_scythe(player)
        pickup(player, "Health Potion")
        type_print("WOW")
    else:
        type_print("... and nothing else. Somebody else got here first!")
    
def start_game():
    player_name = get_name()
    player_health, player_damage = play_beginning()
    player = {
    "name": player_name,
    "damage": player_damage,
    "health": player_health,
    "max_health": player_health,
    "inventory": [],
    "gold": 0,
    }   
    type_print(f"\nWelcome {player_name}!")
    type_print(f"Your starting health is {player_health} and your starting damage is {player_damage}.")
    choose_a_path(player)

start_game()