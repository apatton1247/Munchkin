############### Monster Pokedex ###############

import Monster_Class

########## Level 1 ##########

class Maul_Rat(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Maul Rat"
        self.level = 1
        self.description = "A homely-looking rat wearing a wig and wielding a mallet. A creature from Hell. +3 against Clerics."
        self.undead = False
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "She whacks you. Lose a level."
        self.bad_stuff = lose_level(1, battle_dict)
        self.fight = pass
        self.chase = pass
        self.bias = (clerics(battle_dict), update_monster(3))
        self.good_stuff = pass

#An example of what could go in Monster Methods.
##        def clerics(number, battle_dict):
##            if character.char_class == "Cleric":
##                bias += 3
##            return bias

class Crabs(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Crabs"
        self.level = 1
        self.description = "Not the sea creature. It cannot be Outrun"
        self.undead = False
        self.plant = False
        self.speed = 15
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Discard armor and all items worn below the waist."
        self.bad_stuff = lose_lower_items()
        self.fight = pass
        self.chase = pass
        self.bias = pass
        self.good_stuff = pass

class Potted_Plant(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Potted Plant"
        self.level = 1
        self.description = "A potted plant... thats it. Elves gain an extra Treasure after defeating it."
        self.undead = False
        self.plant = True
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "None. Escape is automatic."
        self.bad_stuff = no_bad_stuff()
        self.fight = pass
        self.chase = auto_escape()
        self.bias = pass
        self.good_stuff = pass

class Lame_Goblin(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Lame Goblin"
        self.level = 1
        self.description = "A small goblin limping with a crutch. +1 to Run Away"
        self.undead = False
        self.plant = False
        self.speed = -1
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "He whacks you with his crutch. Lose a level."
        self.bad_stuff = lose_level(1)
        self.fight = pass
        self.chase = pass
        self.bias = pass
        self.good_stuff = pass

class Drooling_Slime(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Drooling Slime"
        self.level = 1
        self.description = "Yucky slime! +4 against Elves."
        self.undead = False
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Discard the Footgear you are wearing. Lose a level if you are not wearing any Footgear."
        self.bad_stuff = lose_level(1)
        self.fight = pass
        self.chase = pass
        self.bias = (elves(battle_dict), update_monster(4))
        self.good_stuff = pass

########## Level 2 ##########

class Pit_Bull(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Pit Bull"
        self.level = 2
        self.description = "If you can't defeat it, you may distract it (automatic escape) by dropping any wand, pole, or staff. (Fetch, Fido!)"
        self.undead = False
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Fang marks in your butt. Lose 2 levels."
        self.bad_stuff = lose_level(2)
        self.fight = bribe(wand, pole, staff)#we will have to add a boelean attribute to items classes for this
        self.chase = pass
        self.bias = pass
        self.good_stuff = pass

class Flying_Frogs(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Flying Frogs"
        self.level = 2
        self.description = "-1 to Run Away"
        self.undead = False
        self.plant = False
        self.speed = 1
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "They bite!. Lose 2 levels."
        self.bad_stuff = lose_level(2)
        self.fight = pass
        self.chase = pass
        self.bias = pass
        self.good_stuff = pass

class Mr_Bones(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Mr. Bones
        self.level = 2
        self.description = "A skeleton dancing in a top hat. If you must flee you lose a level even if you escape."
        self.undead = True
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "His bony touch costs you 2 levels."
        self.bad_stuff = lose_level(2)
        self.fight = pass
        self.chase = lose_level(1)
        self.bias = pass
        self.good_stuff = pass

class Large_Angry_Chicken(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Large Angry Chicken"
        self.level = 2
        self.description = "Fried Chicken is delicious. Gain an exrtra level if you defeat it with fire or flame."
        self.undead = False
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Very painful pecking. Lose a level."
        self.bad_stuff = lose_level(1)
        self.fight = used_fire(battle_dict)#add fire and flame items/one-shots
        self.chase = pass
        self.bias = pass
        self.good_stuff = pass

class Gelatinous_Octahedron(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Gelatinous Octahedron"
        self.level = 2
        self.description = "+1 to Run Away"
        self.undead = False
        self.plant = False
        self.speed = -1
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Drop all your Big items."
        self.bad_stuff = lose_big_items()
        self.fight = pass
        self.chase = pass
        self.bias = pass
        self.good_stuff = pass

########## Level 3 ##########

class The_Mighty_Germ(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "The Mighty Germ"
        self.level = 3
        self.description = "Really small spec. Halflings can just stomp it, killing it automatically."
        self.undead = False
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Helpless sneezing causes items to fall out of your backpack. Discard 2 items (your choice) from your backpack."
        self.bad_stuff = lose_backpack_item(2)
        self.fight = (halfling(battle_dict), stomp())
        self.chase = pass
        self.bias = pass
        self.good_stuff = pass #may consider using auto_kill() with victory message adaptation here.

class Were_Turtle(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Were-Turtle"
        self.level = 3
        self.description = "A nerdy-looking turtle with a spear. Pursues verrrry slowly. +2 to Run Away"
        self.undead = False
        self.plant = False
        self.speed = -2
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "If you lose a race to the Were_Turtle, you lose your Race. If you were a Half-Breed, lose one non-human race. If you were human already, there's no effect."
        self.bad_stuff = lose_race(character)
        self.fight = pass
        self.chase = pass
        self.bias = pass
        self.good_stuff = pass

class Psycho_Squirrel(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Psycho Squirrel"
        self.level = 3
        self.description = "Will not attack females, or wearers of the Spiked Codpiece."
        self.undead = False
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Lose a level. Speak in a high, squecky voice until your next turn."
        self.bad_stuff = (lose_level(1), font_italic())
        self.fight = bribe(battle_dict, female, spiked_codpiece)
        self.chase = pass
        self.bias = pass
        self.good_stuff = pass

class Pinata(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Pinata"
        self.level = 3
        self.description = "Large paper mache creature. If the Pinata is defeated, each party memeber, in the order you choose, gains one Treasure. It doesn't matter who participated in the combat."
        self.undead = False
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = pinata(character_list)
        self.bad_stuff_description = "The player to your left picks one item that you are using or from your closet. Discard it."
        self.bad_stuff = lose_item()
        self.fight = pass
        self.chase = pass
        self.bias = pass
        self.good_stuff = loot(pinata)

########## Level 4 ##########

class Leperchaun(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Leperchaun"
        self.level = 4
        self.description = "A Leprechaun with limbs falling off. He's gross! +5 against Elves."
        self.undead = False
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "He takes two items from you - one chosen by the player on either side of you."
        self.bad_stuff = lose_item(2)
        self.chase = pass
        self.bias = (elves(battle_dict), update_monster(5))
        self.good_stuff = pass

class Snails_on_Speed(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Snails on Speed"
        self.level = 4
        self.description = "-2 to Run Away"
        self.undead = False
        self.plant = False
        self.speed = 2
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "They steal your treasure. Roll a die and lose that many items or cards in your hand - your choice."
        self.bad_stuff = lose_item(ranint())
        self.fight = pass
        self.chase = pass
        self.bias = pass
        self.good_stuff = pass

class Harpies(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Harpies"
        self.level = 4
        self.description = "Winged creatures playing a harp. They resist magic. +5 against Wizards."
        self.undead = False
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "Their music is really, really bad. Lose 2 levels."
        self.bad_stuff = lose_level(2)
        self.fight = pass
        self.chase = pass
        self.bias = (wizards(battle_dict), update_monster(5))
        self.good_stuff = pass

class Undead_Horse(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Undead Horse"
        self.level = 4
        self.description = "+5 against Dwarves."
        self.undead = False
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "Kicks, bites, and smells awful. Lose 2 levels."
        self.bad_stuff = lose_level(2)
        self.fight = pass
        self.chase = pass
        self.bias = (dwarves(battle_dict), update_monster(5))
        self.good_stuff = pass

########## Level 5 ##########

class Fungus(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Fungus"
        self.level = 5
        self.description = "If the the Fungus becomes Humongous it gains, not the normal +10, but +25! Do not truffle with the Humongous Fungus."
        self.undead = False
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "Elves lose 2 levels. Anyone else loses 1. Double the penalty if the Fungus was Humongous."
        self.bad_stuff = (elves(battle_dict), lose_level(2), lose_level(1))
        self.fight = humongous_fungus(battle_dict)
        self.chase = pass
        self.bias = pass
        self.good_stuff = pass

class Plague_Rats(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Plague Rats"
        self.level = 5
        self.description = "Will flee from Orcs rather than attackng, leaving their treasure behind. Anyone else must fight, and is -1 to Run Away."
        self.undead = False
        self.plant = False
        self.speed = 1
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "Lose 2 levels."
        self.bad_stuff = lose_level(2)
        self.fight = (orcs(battle_dict),flee())#very similar to stomp for The Mighty Germ different victory message
        self.chase = pass
        self.bias = pass
        self.good_stuff = pass #may consider using auto_kill() with victory message adaptation here.

class Teddy_Bear(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Teddy Bear"
        self.level = 5
        self.description = "Digustingly cute. +5 against Orcs."
        self.undead = False
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "Discard your whole backpack. If you discarded more than one item, you may pick up one Treasure while Teddy is cackling over his ill-gotten gains."
        self.bad_stuff = (empty_backpack(character), teddy_is_distracted())
        self.fight = pass
        self.chase = pass
        self.bias = (orcs(battle_dict), update_monster(5))
        self.good_stuff = pass

class Crawling_Hand(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Crawling Hand"
        self.level = 4
        self.description = "A severed hand. If you give the Crawling Hand a Wishing Ring instead of fighting it, it will be your little friend. As a friend it now acts as a small item that gives +3 bonus in combat."
        self.undead = True
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "Undead wedgie! Lose 2 levels."
        self.bad_stuff = lose_level(2)
        self.fight = 
        self.chase = pass
        self.bias = (dwarves(battle_dict), update_monster(5))


########## Level 10 ##########

class Shadow_Nose(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "The Shadow Nose"
        self.description = "Anything affecting the Floating nose works on its undead Shadow, too.  But the shadow won't take bribes."
        self.undead = True
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 3
        self.bad_stuff_description = "You cannot flee. It automatically catches you. Lose 3 levels."
        self.bad_stuff = lose_level(1, battle_dict)
        self.fight = pass
        self.chase = pass
        self.bias = pass
        self.good_stuff = pass
##      if "The Floating Nose" in battle_dict.keys():
##            self.enhancement += 10
##        if "Snot Elemental" in battle_dict.keys():
##            self.enhancement += 10

        

   
  
