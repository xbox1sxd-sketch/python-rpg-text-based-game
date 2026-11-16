import random

from combat import combat, dungeon  # type: ignore
from items import open_chest, pickup, show_inventory, use_potion  # type: ignore
from save_load import delete_save, save_game  # type: ignore
from shops import merchant, shop  # type: ignore
from ui import clear, input_type, pause, type_print  # type: ignore


#Where everything comes back to, the starting 3 places.
def choose_a_path(player):
    save_game(player)
    path = input_type("\nNow, where would you like to go? A. A shimmering city. B. A dark forest. C. Through the swamp. D. Colosseum. I. Inventory P. Drink a health pot R. Rest(10g) ").upper().strip()
    if path == "A":
        clear()
        return shimmering_city(player)
    elif path == "B":
        clear()
        return dark_forest(player)
    elif path == "C":
        clear()
        return swamp(player)
    elif path == "D":
        clear()
        return colosseum(player)
    elif path == "I":
        clear()
        show_inventory(player)
        return choose_a_path(player)
    elif path == "P":
        clear()
        use_potion(player)
        return choose_a_path(player)
    elif path == "R":
        clear()
        return campfire(player)
    else:
        clear()
        type_print("Please choose A. B. C. I. P. or R")
        
        return choose_a_path(player)

#Place where you can heal.. or get jumped lmao
def campfire(player):
    if player["gold"] >= 10:
        if player["health"] >= player["max_health"]:
            type_print("You are already at full health")
        else:
            player["gold"] -= 10
            player["health"] = min(player["max_health"], player["health"] + 30)
            type_print(f"You rest by the fire. You heal 30 hp. You now have {player['health']}/{player['max_health']} health.")
    else:
        type_print("You dont have 10 gold to pay for the fire(BROKIE)")
        type_print("A thief jumps out and attacks you! (shouldnt have came to heal while broke jajaja)")
        return combat(player, 30, 4, "Thief", "Campfire")
    pause()
    return choose_a_path(player)

#Shimmering city the main area
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
        clear()
        type_print("Please ENTER A. B. or C.")
        pause()
        return shimmering_city(player)

#Dark forest where you can fight the bandits
def dark_forest(player):
    clear()
    type_print("You wander into the dark forest..")
    while True:
        choice = input_type("A. Wander around. B. Follow some tracks you see. C. Leave").upper().strip()
        if choice in ("A", "B", "C"):
            break
        type_print("Please choose A, B, or C")
    if choice =="B":
        return bandit_camp(player)
    elif choice == "C":
        return choose_a_path(player)
            
    
    encounter = random.randint(1, 10)
    if 1 <= encounter <= 5:
        type_print("A wolf approaches you!")
        return combat(player, 25, 5, "wolf")
    elif 6 <= encounter <= 8:
        type_print("A goblin approaches you!")
        return combat(player, 50, 8, "goblin")
    elif encounter == 9:
        type_print("A masked man jumps out of a bush!")
        return combat(player, 30, 4, "Thief")    
    else:
        type_print("You discover a treasure chest! How rare!")
        open_chest(player)
        pause()
        return choose_a_path(player)

#Bandit camp, place of miniboss
def bandit_camp(player):
    clear()
    if player.get("bandit_leader_dead"):
        type_print("The camp is abandoned.. theres nothing left.")
        return choose_a_path(player)
    type_print("You see a camp.. they appear to be.. bandits of some sort.")
    type_print("THEY SPOT YOU!")
    choice = input_type("Do you A. Fight, B. Call for their leader, or C. Leave").upper().strip()
    if choice == "A":
        roll = random.randint(1, 10)
        if roll <= 5:
            type_print("A bandit scout runs at you!")
            return combat(player, 40, 8, "Bandit Scout", "BanditCamp")
        elif roll <= 8:
            type_print("A Big boy bandit blocks your path.")
            return combat(player, 60, 10, "Bandit Gangster", "BanditCamp")
        else:
            type_print("A bandit Giant charges at you!")
            return combat(player, 80, 12, "Bandit Giant", "BanditCamp")
    elif choice == "B":
        type_print("The bandits call their leader.")
        type_print("You *DARE* challenge me? He bellows.")
        return combat (player, 120, 15, "Bandit Leader", "BanditCamp")
    elif choice == "C":
        return dark_forest(player)
    else:
        type_print("Please choose A, B, or C.")
        pause()
        return bandit_camp(player)
                       
    
#The witches place, was gonna make it a joke place but decided against that.
def swamp(player):
    clear()
    encounter = random.randint(1, 10)
    if encounter <=3:
        type_print("A large Snake slithers out of the mud!")
        return combat(player, 30, 6, "Swamp Snake", "Swamp")
    elif encounter == 4:
        type_print("A masked man is hiding in the mud and jumps out!")
        return combat(player, 30, 4, "Thief", "Swamp")
    
    while True:
        if player.get("witch_dead"):
            path = input_type("You trek through the swamp. A. The empty Witches hut. B. A seperate secret enterence to the city. C. A graveyard behind the witches house").upper().strip()
            if path in ("A", "B", "C"):
                break
        else:
            path = input_type("You trek through the swamp. Do you go to A. A witches hut. or B. A secret entrance to the city. ").upper().strip()
            if path in ("A", "B"):
                break
        type_print("Please choose A or B")
    if path == "A":
        if player.get("witch_dead"):
            type_print("The witches hut is empty. Shes dead remember?")
            pause()
            return swamp(player)
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
                pause()
                return choose_a_path(player)
            else:
                type_print("Please type A, B, or C.")
                pause()
    elif path == "B":
        type_print("You find a hidden enterence into the city")
        pause()
        return inside_city(player)
    elif path == "C":
        clear()
        return graveyard(player)

#Witch was too boring, so i added this, OH also did you notice the thief everywhere?
def graveyard(player):
    clear()
    type_print("You step into the haunted graveyard. A chill runs down your spine...")
    choice = input_type("A. Dig up the graves looking for loot. B. Explore the crypts. C. Leave").upper().strip()
    if choice == "A":
        roll = random.randint(1, 10)
        if roll <= 4:
            type_print("You dig up the wrong grave! A zombie bursts out.")
            return combat(player, 50, 10, "Zombie", "Graveyard")
        elif roll == 5 and "Cursed Blade" not in player["inventory"]:
            type_print("You dig up a rusted coffin. And find a pitch black sword. It swallows some health for more damage.")
            player["damage"] += 12
            player["max_health"] -= 30
            player["health"] = min(player["health"], player["max_health"])
            pickup(player, "Cursed Blade")
            type_print("You equip the cursed blade(+12 damage, -30max health)")
            pause()
            return graveyard(player)
        elif roll == 6:
            type_print("A thief is looting the tombs! He attacks you!")
            return combat(player, 30, 4, "Thief", "Graveyard")
        else:
            gold_found = random.randint(20, 45)
            player["gold"] += gold_found
            type_print(f"You find a buried chest with {gold_found} gold inside!")
            pause()
            return graveyard(player)
    elif choice == "B":
        roll = random.randint(1, 10)
        if roll <= 5:
            type_print("A skeleton rattles towards you!")
            return combat(player, 40, 8, "Skeleton", "Graveyard")
        else:
            type_print("A ghost floats through the wall!")
            return combat(player, 65, 12, "Wraith", "Graveyard")
    elif choice == "C":
        return choose_a_path(player)
    else:
        type_print("Please choose A, B, or C.")
        pause()
        return graveyard(player)
 
 #Inside of the shimmering city, leads to the dungeon and eventually 'the sealed one' ooooh   
def inside_city(player):
    save_game(player)
    clear()
    type_print("You now sneak past the gates into the shimmering city")
    type_print("It is beautiful, unlike any city you have ever seen.")
    choice = input_type("What do you do? A. Look for the blacksmith. B. Wander around. C. Look at the giant grate. D. Enter the Tavern or E. Leave").upper().strip()
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
        return tavern(player)
    elif choice == "E":
        clear()
        return choose_a_path(player)
    else:
        type_print("Please ENTER A, B, C, or D")
        clear()
        return inside_city(player)

#The tavern where you can eat and gamble
def tavern(player):
    clear()
    type_print("You walk towards the tavern. You already smell the booze and meat.")
    choice = input_type("A. Buy a meal and drink(15g, heals 50hp). B. Arm wrestle for gold. Or C. Leave")
    if choice == "A":
        if player["gold"] >= 15:
            player["gold"] -= 15
            player["health"] = min(player["max_health"], player["health"] + 50)
            type_print(f"You fill your stomach up. Your health is now {player['health']}/{player['max_health']}")
        else:
            type_print("The bartender shakes his head. 'Sorry, I dont serve them poor ones'")
    elif choice == "B":
        if player["gold"] >= 20:
            player["gold"] -= 20
            type_print("A massive wrestler slams his arm onto the table.. you put 20 gold down.")
            if random.randint(1, 20) <= (player["damage"] / 2):
                player["gold"] += 50
                type_print("You destroy him!. The crows boos. You win 50g")
            else:
                type_print("Your arm gives out. The wrestler takes your gold.")
        else:
            type_print("You need 20 gold to make a bet.")
    elif choice == "C":
        return inside_city(player)
    else:
        type_print("please choose A. B. or C")
    pause()
    return tavern(player)

#yea just a little place to get money.. or get robbed
def wander_streets(player):
    clear()
    roll = random.randint(1, 10)
    if roll <= 4:
        gold_found = random.randint(10, 30)
        player["gold"] += gold_found
        type_print(f"You spot a wallet on the floor +{gold_found} gold")
        pause()
        return inside_city(player)
    elif roll <= 7:
        type_print("An angry dude thinks you stole his wallet!")
        return combat(player, 40, 10, "angry dude", "city")
    elif roll == 8:
        type_print("A thief tries to pickpocket you!")
        return combat(player, 30, 4, "Thief", "city")
    else:
        type_print("Nothing worthwhile here")
        pause()
        return inside_city(player)

#Just a village, more options
def village(player):
    save_game(player)
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
        pause()
        return village(player)
    
# local who gives you the lore
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
    pause()
    return village(player)

#just a place full of enemies
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
            return combat(player, 50, 15, "pale child", "HiddenCity")
        elif roll == 7:
            type_print("A thief jumps out!")
            return combat(player, 30, 4, "Thief", "HiddenCity")
        elif roll == 8:
            type_print("A watcher in armour approaches")
            return combat(player, 80, 14, "watcher", "HiddenCity")
        elif roll == 9:
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
        pause()
        return far_underground(player)

#Enterence to the sealed one
def sealed_gate(player):
    clear()
    if player["sealed_one_dead"]:
        type_print("The gate is broken open. Nothing is inside...")
        pause()
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
        pause()
        return sealed_gate(player)

# Colosseum where you fight your way up to a mini-boss
def colosseum(player):
    clear()
    wave = player.get("arena_wave", 0)
    if wave == 0:
        type_print("You enter the grand Colosseum. They mistake you for a participant and you inside.")
    else:
        type_print(f"You are currently on Wave {wave}. You hear the crowd chanting for your death.")
    choice = input_type("A. Fight the next wave. B. Leave the Colosseum.").upper().strip()
    if choice == "A":
        player["arena_wave"] += 1
        next_wave = player["arena_wave"]
        if next_wave == 10:
            type_print("The crowd goes silent... the previous champion steps out!")
            return combat(player, 200, 25, "Arena Champion", "Colosseum")
        enemy_hp = 30 + (next_wave * 15)
        enemy_dmg = 5 + (next_wave * 2)
        type_print(f"A gladiator steps into the arena. (HP: {enemy_hp}, Damage: {enemy_dmg})")
        return combat(player, enemy_hp, enemy_dmg, "Gladiator", "Colosseum")
    elif choice == "B":
        if wave > 0:
            reward = wave * 30
            player["gold"] += reward
            type_print(f"You leave the arena. For surviving {wave} waves, you are awarded {reward} gold!")
            player["arena_wave"] = 0
        else:
            type_print("You chickened out and left the Colosseum")
            
        pause()
        return choose_a_path(player)
    else:
        type_print("Please choose A or B.")
        pause()
        return colosseum(player)
        
#The end of the game.
def sealed_ending(player):
    clear()
    type_print("The sealed one falls. The lanterns go out one by one.")
    type_print("The village is quiet for the first time in a long time.")
    type_print("You climb back up to the surface.")
    type_print("Congratulations! You have completed the game!")
    type_print("\nTHE END\n")
    while True:
        choice = input_type("A. Play again. or B. Close").upper().strip()
        if choice == "A":
            clear()
            delete_save()
            return True
        if choice == "B":
            clear()
            delete_save()
            type_print("THANKS FOR PLAYING!")
            return False
        type_print("Please choose A. or B")