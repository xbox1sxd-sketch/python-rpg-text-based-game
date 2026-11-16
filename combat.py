import random

from items import pickup, use_potion  # type: ignore
from ui import clear, input_type, pause, type_print  # type: ignore


#calculates enemies damage including armour
def calc_enemy_damage(player, enemy_damage):
    base = random.randint(enemy_damage -2, enemy_damage + 2)
    return max(1, base - player.get("armour", 0))

#gets the enemy and its stats, its drops, if you or it dies, and where youll end up if you win
def combat(player, enemy_health, enemy_damage, enemy_name, next = "crossroads", flee_to = None):
    from world import (  # type: ignore
        bandit_camp,
        choose_a_path,
        colosseum,
        dungeon,
        far_underground,
        graveyard,
        inside_city,
        sealed_ending,
        swamp,
        village,
    )
    type_print(f"You encounter a {enemy_name}.")
    type_print(f"It has {enemy_health} health!")
    while enemy_health > 0 and player["health"] > 0:
        choice = input_type("Would you like to A. Attack, B. Flee, C. Use a Potion, or I. Inventory ").strip().upper()
        if choice == "A":
            if random.randint(1, 10) == 1:
                type_print("You swing and you miss! Strike out!")
                damage = 0
            else:
                if random.randint(1, 10) == 1:
                    damage = player["damage"] * 2
                    type_print(f" WOW you did a crit! You did {damage} damage!")
                else:
                    damage = player["damage"]
                type_print(f"You did {damage} damage!")
            enemy_health = max(0, enemy_health - damage)
            type_print(f"It has {enemy_health} health left!")
            damage_dealt = calc_enemy_damage(player, enemy_damage)
            if enemy_health > 0:
                player["health"] = max(0, player["health"] - damage_dealt)
                type_print(f"The {enemy_name} did {damage_dealt} damage! You have {player['health']} health left!")
                if enemy_name == "Thief" and player["gold"] > 0:
                    stolen = 15
                    if player["gold"] < 15:
                        stolen = player["gold"]
                    player["gold"] -= stolen
                    type_print(f"The thief grabs {stolen} gold from your bag!")
                
        elif choice == "B":
            type_print("You scream and run away")
            base_damage =  calc_enemy_damage(player, enemy_damage)
            flee_damage = max(1, base_damage) * 2
            player["health"] = max(0, player["health"] - flee_damage)
            type_print(f"The {enemy_name} hits you as you flee, dealing {flee_damage} damage! You have {player['health']} health left.")
            if player["health"] <= 0:
                break
            if enemy_name in ("Gladiator", "Arena Champion"):
                player["arena_wave"] = 0
                type_print("You fled the arena! Your win streak is set to 0!")
            target = flee_to if flee_to is not None else next
            if target == "city":
                return inside_city(player)
            elif target == "Dungeon":
                return dungeon(player)
            elif target == "HiddenCity":
                return far_underground(player)
            elif target == "BanditCamp":
                return bandit_camp(player)
            elif target == "Swamp":
                return swamp(player)
            elif target == "Graveyard":
                return graveyard(player)
            elif target == "Campfire":
                return choose_a_path(player)
            return choose_a_path(player)
        elif choice == "C":
            if use_potion(player) == False:
                type_print("You fumble in your pack and waste your turn :sob:")
            damage_dealt = calc_enemy_damage(player, enemy_damage)
            player["health"] = max(0, player["health"] - damage_dealt)
            type_print(f"The {enemy_name} did {damage_dealt} damage while you were fooling around! you have {player['health']} health left! ")
        elif choice == "I":
            from items import show_inventory
            show_inventory(player)
            continue
        else:
            type_print("Please choose A, B, C, or I")
    if enemy_health <= 0:
        type_print("YOU WON!")
        if enemy_name == "Dungeon Guardian":
            player["guardian_dead"] = True
            player["armour"] += 3
            pickup(player, "Guardian Shield")
            type_print("You defeated the Guardian! You took its shield (+3 armour)")
            pause()
            if next == "Dungeon":
                player["dungeon_floor"] += 1
                return dungeon(player)
        if enemy_name == "Warden":
            player["warden_dead"] = True
            player["damage"] += 7
            pickup(player, "Warden's spear")
            type_print("The warden collapses. The gold door grinds open behind it.")
            pause()
            player["dungeon_floor"] = 6
            return village(player)
        if enemy_name == "The Sealed One":
            player["sealed_one_dead"] = True
            pause()
            return sealed_ending(player)
        enemy_drop(player, enemy_name)
        pause()
        if enemy_name == "Bandit Leader":
            player["bandit_leader_dead"] = True
            player["damage"] += 6
            pickup(player, "Bandit's Bat")
            type_print("You defeat the bandit Leader! You take his big bat.")
            pause()
            return bandit_camp(player)
        if enemy_name == "Witch":
            player["witch_dead"] = True
            pickup(player, "Witch's Charm")
            type_print("The witch dies. The fog lifts off the swamp, revealing a massive GraveYard!")
            pause()
            return swamp(player)
        if enemy_name == "Gladiator" and random.randint(1, 10) <= 4:
            if "Gladiator's Sword" not in player["inventory"]:
                player["damage"] += 4
                pickup(player, "Gladiator's Sword")
                type_print("You take the Gladiator's Sword and hold it high! (+4 dmg)")
                pause()
        
        if next == "city":
            return inside_city(player)
        elif next == "Dungeon":
            player["dungeon_floor"] += 1
            return dungeon(player)
        elif next == "HiddenCity":
            return far_underground(player)
        elif next == "BanditCamp":
            return bandit_camp(player)
        elif next == "Colosseum":
            return colosseum(player)
        elif next == "Swamp":
            return swamp(player)
        elif next == "Graveyard":
            return graveyard(player)
        return choose_a_path(player)
    elif player["health"] <= 0:
        type_print("You lost LOL")
        type_print("You wake up at the crossroads. Your bag feels lighter you think you lost some gold.")
        player["health"] = player["max_health"] // 2
        player["gold"] = player["gold"] // 2
        player["dungeon_floor"] = 0
        player["arena_wave"] = 0
        pause()
        return choose_a_path(player)
    
#Calculates how much gold you get if you kill an enemy, also health potions.
def enemy_drop(player, enemy_name):
    roll = random.randint(1, 100)
    if roll <= 30:
        type_print(f"The {enemy_name} was holding something...")
        pickup(player, "Health Potion")
    elif roll <= 60:
        gold_found = random.randint(10, 20)
        player["gold"] += gold_found
        type_print(f"You got {gold_found} gold from that corpse!")

        
#Handles the warden boss fight
def boss_fight(player):
    if player["warden_dead"] == True:
        type_print("The gold door stands silent. Nothing is behind it now.")
        pause()
        return dungeon(player)
    clear()
    type_print("The door slides open, the ground rumbles as the thing behind it awakens...")
    type_print("The warden RISES")
    return combat(player, 100, 12, "Warden", "Dungeon")      

#Makes the dungeon where you can fight a bunch of enemies
def dungeon(player):
    from world import inside_city, village  # type: ignore
    clear()
    floor = player["dungeon_floor"]
    if player["warden_dead"] and floor == 0:
        type_print("The tunnel is quiet, the tunnel to the Sealed Village is Open")
        choice = input_type("A. Walk straight to the village, B. Fight your way down again, or C. Leave").strip().upper()
        if choice == "A":
            clear()
            return village(player)
        elif choice == "B":
            clear()
        elif choice == "C":
            return inside_city(player)
        else:
            type_print("Please choose A, B, or C.")
            pause()
            return dungeon(player)
    if floor >= 6:
        return village(player)
    if floor == 5:
        if player["warden_dead"]:
            player["dungeon_floor"] = 6
            return village(player)
        return boss_fight(player)
    if floor > 0:
        type_print(f"You stand in the tunnel, {floor} floor(s) under the city.")
        choice = input_type("A.) Fight whats ahead. B: Climb back up (lose all dungeon progress)").upper().strip()
        if choice == "B":
            player["dungeon_floor"] = 0
            type_print("You climb back up. Losing all your progress.")
            pause()
            clear()
            return inside_city(player)
        elif choice != "A":
            type_print("Please choose A. or B.")
            pause()
            return dungeon(player)
    clear()
        
    if floor == 0 :
            type_print("something scurries past your feet")
            return combat(player, 20, 5, "crawler", "Dungeon")
    elif floor == 1:
            type_print("A figure stumbles out")
            return combat(player, 35, 7, "Shanker", "Dungeon")
    elif floor == 2:
            type_print("Something drags itself to you")
            return combat(player, 45, 6, "trash thing", "Dungeon")
    elif floor == 3:
            if not player.get("guardian_dead"):
                type_print("A massive armored figure blocks the door.")
                return combat(player, 80, 12, "Dungeon Guardian", "Dungeon")
            else:
                type_print("Something drops from above")
                return combat(player, 55, 10, "haunter", "Dungeon")
    else:
            type_print("two shankers step out side by side")
            return combat(player, 70, 12, "twin shankers", "Dungeon")