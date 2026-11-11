import random

from combat import combat, dungeon  # type: ignore
from items import open_chest, show_inventory, use_potion  # type: ignore
from save_load import delete_save, save_game  # type: ignore
from Shops import merchant, shop  # type: ignore
from ui import clear, input_type, type_print  # type: ignore


def choose_a_path(player):
    save_game(player)
    path = input_type("\nNow, where would you like to go? A. A shimmering city. B. A dark forest. C. Through the swamp. I. Inventory P. Drink a health pot ").upper().strip()
    if path == "A":
        clear()
        return shimmering_city(player)
    elif path == "B":
        clear()
        return dark_forest(player)
    elif path == "C":
        clear()
        return swamp(player)
    elif path == "I":
        clear()
        show_inventory(player)
        return choose_a_path(player)
    elif path == "P":
        clear()
        use_potion(player)
        return choose_a_path(player)
    else:
        clear()
        type_print("Please choose A. B. C. I. or P")
        
        return choose_a_path(player)


def shimmering_city(player):
    clear()
    type_print("You make your way down to the city... unfortunately you somehow get stopped by the guard for not having any ID.")
    guards = input_type("Do you A. Turn back to the crossroads. B. Say you'll turn back and try to sneak past them. C. Fight ").upper().strip()
    if guards == "A":
        clear()
        return choose_a_path(player)
    elif guards == "B":
        clear()
        type_print("This managed to work. You are now inside the city.")
        return inside_city(player)
    elif guards == "C":
        clear()
        return combat(player, 30, 5, "guard", "city", "crossroads")
    else:
        type_print("Please enter A. B. or C.")
        input_type("Press enter to continue")
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
        input_type("Press enter to continue")
        return choose_a_path(player)

def swamp(player):
    while True:
        path = input_type("You trek your way through the swamp. There you see two things, which do you go to? A. A Witches hut. or B. A seperate secret enterence to the city.").upper().strip()
        if path in ("A", "B"):
            break
        type_print("Please choose A or B")
    if path == "A":
        while True:
            witch = input_type("You make your way into the witches hut. Inside you see the witch sleeping. Do you A. Kill her. or B. Wake her up? or C. Leave ").upper().strip()
            if witch == "A":
                type_print("You tried to kill her, but failed as she suddenly rolled over. This woke her up.")
                return combat(player, 40, 10, "Witch")
            elif witch == "B":
                type_print("You really scared her. She's enraged.")
                return combat(player, 50, 12, "Witch")
            elif witch == "C":
                type_print("You decided to leave (very smart)")
                input_type("Press enter to continue")
                return choose_a_path(player)
            else:
                type_print("Please type A, B, or C.")
    elif path == "B":
        type_print("You find a hidden enterence into the city")
        input_type("Press enter to continue")
        return inside_city(player)


def inside_city(player):
    clear()
    type_print("You now sneak past the gates into the shimmering city")
    type_print("It is beautiful, unlike any city you have ever seen.")
    choice = input_type("What do you do? A. Look for the blacksmith. B. Wander around. C. Look at the giant grate or D. Leave").upper().strip()
    if choice == "A":
        clear()
        return shop(player)
    elif choice == "B":
        clear()
        return wander_streets(player)
    elif choice == "C":
        clear()
        return dungeon(player)
    elif choice == "D":
        clear()
        return choose_a_path(player)
    else:
        type_print("Please enter A, B, C, or D")
        clear()
        return inside_city(player)


def wander_streets(player):
    clear()
    roll = random.randint(1, 10)
    if roll <= 4:
        gold_found = random.randint(10, 30)
        player["gold"] += gold_found
        type_print(f"You spot a wallet on the floor +{gold_found} gold")
        input_type("Press enter to continue")
        return inside_city(player)
    elif roll <= 7:
        type_print("An angry dude thinks you stole his wallet!")
        return combat(player, 40, 10, "angry dude", "city")
    else:
        type_print("Nothing worthwhile here")
        input_type("Press enter to continue")
        return inside_city(player)


def village(player):
    clear()
    type_print("The tunnel opens into a street...?")
    type_print("Above you, far above, you can hear the ground shake above you.")
    choice = input_type("What do you do? A. Visit the market B. Talk to a local C. Keep walking or D. Try to go back up").strip().upper()
    if choice == "A":
        clear()
        return merchant(player)
    elif choice == "B":
        clear()
        return local(player)
    elif choice == "C":
        clear()
        return far_underground(player)
    elif choice == "D":
        player["dungeon_floor"] = 0
        clear()
        return inside_city(player)
    else:
        type_print("Please choose A, B, C, or D" )
        input_type("Press enter to continue")
        return village(player)
    
    
def local(player):
    clear()
    type_print("A thin man leans against a wall. He looks like he hasnt slept in a while...")
    type_print("'You killed the warden' he says 'we heard it fall from here'.")
    type_print("'Do you know how much it did for us?'")
    choice = input_type("A. It was guarding this place B. It was keeping something out. or C. Say nothing").upper().strip()
    if choice == "A":
        type_print("'No,' he says. 'it was keeping something in'")
    elif choice == "B":
        type_print("'Wrong way round' he says 'it was keeping it from getting out'")
    else:
        type_print("Dont matter, he says 'You should know either way'")
    type_print("'When the old city was sealed, the warden was used as a lock to keep it out. The sealed one is what the lock was for'")
    type_print("'Now the lock is broken. It will awaken soon.'")
    input_type("Press enter to continue")
    return village(player)

def far_underground(player):
    clear()
    type_print("The streets narrow.")
    choice = input_type("A. Walk deeper. B. Approach the sealed gate. or C. go back.").upper().strip()
    if choice == "A":
        clear()
        roll = random.randint(1, 10)
        if roll <= 2:
            type_print("A pale figure steps out of a doorway.")
            return combat(player, 40, 12, "sealed child", "HiddenCity")
        elif roll <= 4:
            type_print("Something flys through the walls.")
            return combat(player, 55, 16, "ghoul", "HiddenCity")
        elif roll <= 6:
            type_print("A child-shaped shadow runs past you.")
            return combat(player, 50, 15, "Pale Child", "HiddenCity")
        elif roll <= 7:
            type_print("A watcher in armor approaches")
            return combat(player, 80, 14, "Watcher", "HiddenCity")
        elif roll <= 8:
            type_print("A small thing crawls over.")
            return combat(player, 70, 12, "better crawler", "HiddenCity")
        else:
            type_print("A hunched thing crawls over.")
            return combat(player, 80, 13, "elder crawler", "HiddenCity")
    elif choice == "B":
        clear()
        return sealed_gate(player)
    elif choice == "C":
        clear()
        return village(player)
    else:
        type_print("Please choose A, B, or C.")
        input_type("Press enter to continue")
        return far_underground(player)

def sealed_gate(player):
    clear()
    if player["sealed_one_dead"]:
        type_print("The gate is broken open. Nothing is inside...")
        input_type("Press enter to continue")
        return far_underground(player)
    type_print("An enormous stone gate stands here.")
    type_print(" Many chains lay snapped on the floor. A couple remain.")
    type_print("You hear something breathe.")
    choice = input_type("A. Break the last chains. B. Leave").upper().strip()
    if choice == "A":
        clear()
        type_print("The last chain falls. The gate opens")
        type_print("A shape appears, it has too many arms.")
        type_print("It speaks")
        type_print("'You freed me, an unwise decision.'")
        return combat(player, 200, 16, "The Sealed One", "HiddenCity")
    elif choice == "B":
        clear()
        return far_underground(player)
    else:
        type_print("Please choose A, or B")
        input_type("Press enter to continue")
        return sealed_gate(player)
    
    
def sealed_ending(player):
    clear()
    type_print("The sealed one falls. The lanterns go out one by one.")
    type_print("The village is quiet for the first time in a long time.")
    type_print("You climb back up to the surface.")
    type_print("Congratulations! You have completed the game!")
    type_print("\nTHE END\n")
    while True:
        choice = input_type("A. Play again. or B. Close")
        if choice == "A":
            clear()
            return True
        if choice == "B":
            clear()
            delete_save()
            type_print("THANKS FOR PLAYING!")
            return False
        type_print("Please choose A. or B").upper().strip()