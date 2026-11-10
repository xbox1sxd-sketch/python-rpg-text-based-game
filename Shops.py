from items import pickup  # type: ignore
from ui import clear, input_type, type_print  # type: ignore


def shop(player):
    from world import inside_city  # type: ignore
    clear()
    type_print("An exhausted looking blacksmith looks up from this anvil? 'What'll it be' he says")
    type_print(f"You have {player['gold']} gold (earn more from fighting).")
    choice = input_type("A: A health potion (10g). B: A Gold Scythe (+3 dmg, 30g) Or C: Iron Dagger (+1 dmg, 15g) D: War Axe (+5 dmg, 60g) E: Leave ").upper().strip()
    if choice == "A":
        if player["gold"] >= 10:
            player["gold"] -= 10
            pickup(player, "Health Potion")
            input_type("Press enter to continue")
            return shop(player)
        else:
            type_print("You don't have enough gold.")
            input_type("Press enter to continue")
            clear()
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
            type_print("You don't have enough gold :(")
            input_type("Press enter to continue")
            return shop(player)
    elif choice == "C":
        if "Iron Dagger" in player["inventory"]:
            type_print("You already have one")
            input_type("Press enter to continue")
            return shop(player)
        if player ["gold"] >= 15:
            player["gold"] -= 15
            player["damage"] += 1
            type_print(f"Your damage is now {player['damage']}")
            pickup(player, "Iron Dagger")
            input_type("Press enter to continue")
            return shop(player)
        else:
            type_print("You don't have enough gold :(")
            input_type("Press enter to continue")
            clear()
            return shop(player)
    elif choice == "D":
        if "War Axe" in player["inventory"]:
            type_print("You cant buy another")
            input_type("Press enter to continue")
            return shop(player)
        if player["gold"] >= 60:
            player["gold"] -= 60
            player["damage"] += 5
            type_print(f"Your damage is now {player['damage']}")
            pickup(player, "War Axe")
            input_type("Press enter to continue")
            return shop(player)
        else:
            type_print("You don't have enough gold :(")
            input_type("Press enter to continue")
            return shop(player)
    elif choice == "E":
        return inside_city(player)
    else:
        type_print("Please choose A, B, C, D, or E")
        input_type("Press enter to continue")
        return shop(player)


def merchant(player):
    from world import village  # type: ignore
    clear()
    type_print("An old woman sits behind a counter. Her eyes are pale, she looks tired.")
    type_print("'You came from up there' she says. Haven't seen one of yem since the 3rd epoch.")
    type_print(f"You have {player['gold']} gold.")
    choice = input_type("A.) Health potion(8g). B.) Whetstone(+2 dmg, 40g) C.) Iron Heart(+25 max health, 50g) D.) Leave").strip().upper()
    if choice == "A":
        if player["gold"] >= 8:
            player["gold"] -= 8
            pickup(player, "Health Potion")
            input_type("Press enter to continue")
            return merchant(player)
        else:
            type_print("You don't have enough gold")
            input_type("Press enter to continue")
            return merchant(player)
    elif choice == "B":
        if player ["whetstone_bought"]:
            type_print("'I've already used the whetstone for you' says the merchant.")
            input_type("Press enter to continue")
            return merchant(player)
        if player["gold"] >= 40:
            player["whetstone_bought"] = True
            player["gold"] -= 40
            player["damage"] += 2
            type_print(f"She sharpens your weapon. Your damage is now {player['damage']}")
            input_type("Press enter to continue")
            return merchant(player)
        else:
            type_print("You don't have enough gold")
            input_type("Press enter to continue")
            return merchant(player)
    elif choice == "C":
        if player["iron_heart_bought"]:
            type_print("'You've already bought one' she says")
            input_type("Press enter to continue")
            return merchant(player)
        if player["gold"] >= 50:
            player["iron_heart_bought"] = True
            player["gold"] -= 50
            player["max_health"] += 25
            player["health"] += 25
            type_print(f"She hands you some mercury in a bottle and tells you to drink up. Your max health is now {player['max_health']}")
            input_type("Press enter to continue")
            return merchant(player)
        else:
            type_print("You don't have enough gold")
            input_type("Press enter to continue")
            return merchant(player)

    elif choice == "D":
        clear()
        return village(player)
    else:
        type_print("Please choose A, B, C, or D.")
        input_type("Press enter to continue")
        return merchant(player)
