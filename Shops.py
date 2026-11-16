import random

from items import pickup  # type: ignore
from save_load import save_game
from ui import clear, input_type, pause, type_print  # type: ignore


def can_afford(player, price):
    if player["gold"] >= price:
        player["gold"] -= price
        return True
    else:
        type_print("You don't have enough gold")
        pause()
        return False

#The shop. Sells you many goods, however they are on the cheaper side.
def shop(player):
    from world import inside_city  # type: ignore
    clear()
    sale = random.randint(1, 10) <= 2
    while True:
        clear()
        if sale:
            type_print("TAX DAY! The blacksmith is low on money and desperate for gold! Everything is 10g cheaper!")
        type_print("An exhausted looking blacksmith looks up from this anvil? 'What'll it be' he says")
        type_print(f"You have {player['gold']} gold (earn more from fighting).")
        choice = input_type("A. A health potion (10g). B. A Gold Scythe (+3 dmg, 30g) Or C. Iron Dagger (+1 dmg, 15g) D. War Axe (+5 dmg, 60g) G. Leather Armour(+2 armour, 20g) H. Iron armour(+4 armour, 50g) J. Katana(8dmg 150g) K. Super Shield(+6 armor, 200g) F. Sell Weapons I. inventory or E: Leave ").upper().strip()
        if choice == "A":
            price = 10
            if can_afford(player, price):
                save_game(player)
                pickup(player, "Health Potion")
                pause()
        elif choice == "B":
            if "Gold Scythe" in player["inventory"]:
                type_print("You cant buy another")
                pause()
                continue
            price = 20 if sale else 30
            if can_afford(player, price):
                save_game(player)
                player["damage"] += 3
                type_print(f"Congrats! Your damage is now {player['damage']}")
                pickup(player, "Gold Scythe")
                pause()
        elif choice == "C":
            if "Iron Dagger" in player["inventory"]:
                type_print("You already have one")
                pause()
                continue
            price = 5 if sale else 15
            if can_afford(player, price):
                save_game(player)
                player["damage"] += 1
                type_print(f"Your damage is now {player['damage']}")
                pickup(player, "Iron Dagger")
                pause()
        elif choice == "D":
            if "War Axe" in player["inventory"]:
                type_print("You cant buy another")
                pause()
                continue
            price = 50 if sale else 60
            if can_afford(player, price):
                save_game(player)
                player["damage"] += 5
                type_print(f"Your damage is now {player['damage']}")
                pickup(player, "War Axe")
                pause()
        elif choice == "G":
            if "Leather Armour" in player["inventory"]:
                type_print("You already have this armour")
                pause()
                continue
            if player["armour"] >= 4:
                type_print("You have better armour already numbskull")
                pause()
                continue
            price = 10 if sale else 20
            if can_afford(player, price):
                save_game(player)
                player["armour"] = max(player["armour"], 2)
                player["inventory"].append("Leather Armour")
                type_print(f"Your armour is now {player['armour']}")
                pause()
        elif choice == "H":
            if "Iron Armour" in player["inventory"]:
                type_print("You already have this idiot")
                pause()
                continue
            if player["armour"] >= 4:
                type_print(" You already have equal or better armour")
                pause()
                continue
            price = 40 if sale else 50
            if can_afford(player, price): 
                save_game(player)
                player["armour"] = max(player["armour"], 4)
                player["inventory"].append("Iron Armour")
                type_print(f"Your armour is now {player['armour']}")
                pause()
        elif choice == "J":
            if "Katana" in player["inventory"]: 
                type_print("You already have the katana")
                pause()
            else:
                price = 140 if sale else 150
                if can_afford(player, price): 
                    save_game(player)
                    player["damage"] += 8
                    pickup(player, "Katana")
                    type_print(f"Your damage is now {player['damage']}")
                    pause()
        elif choice == "K":
            if "Super Shield" in player["inventory"]:
                type_print("You already have the super shield!")
                pause()
            else:
                price = 190 if sale else 200
                if can_afford(player, price):
                    save_game(player)
                    player["armour"] += 6
                    pickup(player, "Super Shield")
                    type_print(f"Your armour is now {player['armour']}")
                    pause()
        elif choice == "E":
            return inside_city(player)
        elif choice == "I":
            from items import show_inventory
            show_inventory(player)
        elif choice == "F":
            sell_weapon(player)
        else:
            type_print("Please choose a valid option.")
            pause()


#The merchant. Sells you many higher quality goods.
def merchant(player):
    from world import village  # type: ignore
    while True:
        clear()
        type_print("An old woman sits behind a counter. Her eyes are pale, she looks tired.")
        type_print("'You came from up there' she says. Haven't seen one of yem since the 3rd epoch.")
        type_print(f"You have {player['gold']} gold.")
        choice = input_type("A. Health potion(8g). B. Whetstone(+2 dmg, 40g) C. Iron Heart(+25 max health, 50g) D. Leave F. Sell weapons or I. Inventory").strip().upper()
        if choice == "A":
            if player["gold"] >= 8:
                player["gold"] -= 8
                pickup(player, "Health Potion")
                pause()
            else:
                type_print("You don't have enough gold")
                pause()
        elif choice == "B":
            if player ["whetstone_bought"]:
                type_print("'I've already used the whetstone for you' says the merchant.")
                pause()
                continue
            if player["gold"] >= 40:
                player["whetstone_bought"] = True
                player["gold"] -= 40
                player["damage"] += 2
                type_print(f"She sharpens your weapon. Your damage is now {player['damage']}")
                pause()
            else:
                type_print("You don't have enough gold")
                pause()
        elif choice == "C":
            if player["iron_heart_bought"]:
                type_print("'You've already bought one' she says")
                pause()
                continue
            if player["gold"] >= 50:
                player["iron_heart_bought"] = True
                player["gold"] -= 50
                player["max_health"] += 25
                player["health"] += 25
                type_print(f"She hands you some mercury in a bottle and tells you to drink up. Your max health is now {player['max_health']}")
                pause()
            else:
                type_print("You don't have enough gold")
                pause()
        elif choice == "I":
            from items import show_inventory
            show_inventory(player)
        elif choice =="F":
            sell_weapon(player)
        elif choice == "D":
            clear()
            return village(player)
        else:
            type_print("Please choose A. B. C. or D.")
            pause()


#Handles the selling of each weapon. Im sure this could be more optimized... gotta figure that out
def sell_weapon(player):
    clear()
    type_print("Which weapon would you like to sell back?")
    type_print("A. Iron Dagger (sells for 7g)")
    type_print("B. Gold Scythe (sells for 15g)")
    type_print("C. War Axe (sells for 30g)")
    type_print("D. Silver Scythe (sells for 10g)")
    type_print("E. Sell Bandit's Bat (sells for 40g)")
    type_print("F. Sell Katana (sells for 75g)")
    type_print("G. Super Shield (sells for 100g)")
    type_print("H. Gladiator's Sword (sells for 20g)")
    type_print("L. Leave")
    choice = input_type("> ").upper().strip()
    if choice == "A" and "Iron Dagger" in player["inventory"]:
        player["inventory"].remove("Iron Dagger")
        player["damage"] -= 1
        player["gold"] += 7
        type_print("Sold iron dagger for 7 gold. Your damage decreased.")
    elif choice == "B" and "Gold Scythe" in player["inventory"]:
        player["inventory"].remove("Gold Scythe")
        player["damage"] -= 3
        player["gold"] += 15
        type_print("Sold Gold Scythe for 15 gold. Your damage decreased.")
    elif choice == "C" and "War Axe" in player["inventory"]:
        player["inventory"].remove("War Axe")
        player["damage"] -= 5
        player["gold"] += 30
        type_print("Sold war Axe for 30 gold. Your damage decreased.")
    elif choice == "D" and "Silver Scythe" in player["inventory"]:
        player["inventory"].remove("Silver Scythe")
        player["damage"] -= 2
        player["gold"] += 10
        type_print("Sold Silver Scythe for 10 gold. Your damage decreased.")
    elif choice == "E" and "Bandit's Bat" in player["inventory"]:
        player["inventory"].remove("Bandit's Bat")
        player["damage"] -= 6
        player["gold"] += 40
        type_print("Sold Bandit's Bat for 40 gold. Your damage decreased.")
    elif choice == "F" and "Katana" in player["inventory"]:
        player["inventory"].remove("Katana")
        player["damage"] -= 8
        player["gold"] += 75
        type_print("Sold Katana for 75 gold. Your damage decreased.")
    elif choice == "G" and "Super Shield" in player["inventory"]:
        player["inventory"].remove("Super Shield")
        player["armour"] -= 6
        player["gold"] += 100
        type_print("Sold Super Shield for 100 gold. Your armour decreased.")
    elif choice == "H" and "Gladiator's Sword" in player["inventory"]:
        player["inventory"].remove("Gladiator's Sword")
        player["damage"] -= 4
        player["gold"] += 20
        type_print("Sold Gladiator's Sword for 20 gold. Your damage decreased.")
    elif choice == "L":
        return
    else:
        type_print("Either, you dont have that weapon, or typed the wrong letter. Anyway, im dissappointed.")
    pause()
