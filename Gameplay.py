from Character_Class import *
from Monster_Class import *
#from Monster_Pokedex import *
from Curse_Compendium import *
from random import randint
from inspect import getmembers
    
#Runs gameplay

character_list = []
door_deck = []
door_deck_discard = []
treasure_deck = []
treasure_deck_discard = []
game_not_over = True

#Adds characters to the game.  To be called at the beginning of the game
# and may be called if new characters wish to enter mid-game.
def add_characters():

    num_characters = input("How many characters are in the garrison? ")
    while not num_characters.isnumeric():
        num_characters = input("Please enter a number of characters. ")
    else:
        num_characters = int(num_characters)

    for character_number in range(len(character_list), len(character_list) + num_characters):
        name = input("\nCharacter %d Name: " % (character_number + 1))
        gender = input("Character %d Gender: " % (character_number + 1))
        character = Character(name, gender)
        character_list.append(character)

#Should be able to use inspect.getmembers to return a list of classes, value pairs from whatever
# module (.py file) we pass it.  For example, if module = Monster_Pokedex, one of the value pairs
# will be ("Maul_Rat", Class).  Then if the correctly-formatted name we pass it matches up with any
# class names in the file, it should use getattr to call the class's __init__ method and return the
# resulting card object into card_obj, which gets returned to whatever calls it.  If this function
# runs through the whole module it's given and doesn't find any matching class names, it returns None.
def card_creation(card_name, module):
    for name, value in inspect.getmembers(module):
        if name == card_name:
            card_obj = getattr(module, card_name)()
            return card_obj
    else:
        return None
    

#Reads in the card names from appropriate text files, creates card objects, and populates
# the door and treasure decks with those card objects.
def create_decks():
    door_card_list = []
    with open("door_card_list.txt", "r") as door_card_file:
        for line in door_card_file:
            door_card_list.append(line.rstrip())
    print("Door card list: ", door_card_list)

    #TBD - create DoorCard objects
    #The idea here is we populate places_to_look with the modules (.py files) we want it to look in to
    # find the classes that match up with the string input, then call card_creation to search through
    # that module.  If a matching class is not found in the module, the next module is searched, until
    # an object is returned (the first "else" below, which breaks out of the inner for-loop and moves on
    # to the next card), or no matching class is found in any of the places_to_look (the second "else"),
    # at which time a message of unavailability is given and the card removed from play.
    for card in door_card_list:
        card_name = card.replace(" ", "_")

        places_to_look = [Monster_Pokedex, Curse_Compendium]
        for place in places_to_look:
            card_obj = card_creation(card_name, place)
            if card_obj == None:
                continue
            else:
                card = card_obj
                break
        else:
            print("No such card as %s listed" % (card))
            door_card_list.remove(card)

    
    door_list_len = len(door_card_list)
    for x in range(door_list_len):
        next_card_index = randint(0, len(door_card_list)-1)
        door_deck.append(door_card_list.pop(next_card_index))
    if not door_card_file.closed:
        door_card_file.close()
    print("Door deck: ", door_deck)

    treasure_card_list = []
    with open("treasure_card_list.txt", "r") as treasure_card_file:
        for line in treasure_card_file:
            treasure_card_list.append(line.rstrip())
    print("Treasure card list: ", treasure_card_list)

    #TBD - create TreasureCard objects
    #The idea here is we populate places_to_look with the modules (.py files) we want it to look in to
    # find the classes that match up with the string input, then call card_creation to search through
    # that module.  If a matching class is not found in the module, the next module is searched, until
    # an object is returned (the first "else" below, which breaks out of the inner for-loop and moves on
    # to the next card), or no matching class is found in any of the places_to_look (the second "else"),
    # at which time a message of unavailability is given and the card removed from play.
    for card in treasure_card_list:
        card_name = card.replace(" ", "_")
        #TBD - create .py files in which to look for Treasure Card classes
        places_to_look = []
        for place in places_to_look:
            card_obj = card_creation(card_name, place)
            if card_obj == None:
                continue
            else:
                card = card_obj
                break
        else:
            print("No such card as %s listed" % (card))
            treasure_card_list.remove(card)

    
    treasure_list_len = len(treasure_card_list)
    for x in range(treasure_list_len):
        next_card_index = randint(0, len(treasure_card_list)-1)
        treasure_deck.append(treasure_card_list.pop(next_card_index))
    if not treasure_card_file.closed:
        treasure_card_file.close()
    print("Treasure deck: ", treasure_deck)

    return door_deck, treasure_deck

#Whenever a character has to (re)supply at the garrison, this function places
# 4 DoorCard objects and 4 TreasureCard objects in their backpack
def get_supplies(character, door_deck, treasure_deck):

    supplies = []
    for x in range(4):
      supplies.append(door_deck.pop(0))
    for x in range(4):
      supplies.append(treasure_deck.pop(0))
    for thing in supplies:
        character.backpack.append(thing)

#Shuffles a deck's discard pile if the deck is completely empty, returning a new draw deck
def shuffle(discards):
  #Once we have a discard deck, shuffle it similarly to how we shuffled the start decks
  pass

def open_door(character, door_deck):
    print(character.backpack)
    if door_deck[0].type == "monster":
        monster = door_deck.pop(0)
        battle(character, monster)
    elif door_deck[0].type == "curse":
        #TBD - create cases for curse cards
        pass
    else:
        #TBD - create cases for action cards, maybe other types?
        pass

def make_battle_dict():
    battle_dict = {}
    battle_dict["monster"] = {}
    battle_dict["character"] = {}
    battle_dict["monster"]["monster one-shots"] = {}
    battle_dict["character"]["character one-shots"] = {}

def battle_loop()
    #During battle, the player(s) fighting the monster get to act; then in turn order, the players not fighting
    # the monster get to interfere; every time a character interferes, the loop goes back to the player(s)
    # fighting the monster, and they get a chance to act again, and play continues to the next character after
    # the one who interfered.  If a character does not interfere on their turn, play passes to the next character
    # not fighting the monster.  After a full round of no interference by the non-fighting characters, the
    # fighting characters get one more chance to act, and if they do the loop restarts.
    

def battle(character, monster):
    battle_dict["monster"][monster] = monster.battle_strength
    battle_dict["character"][character] = character.battle_strength

    battle_loop(battle_dict, character_list)
    #Battle phases:
    #   Preliminary phase (Dryad, Tongue Demon, anything that happens immediately)
    #   Update phase (monster's biases/strength get updated / calculated)
    #   Pursuit phase (decides if a monster will not pursue, finds out if character will pursue anyway)
    #   Fight phase (calculates / announces current monster vs character standing)
    #   Loop: for each character, starting with the next character and going to each other character in turn,
    #    and if nobody interferes, going back to the character in the fight.  Only after a full loop of no
    #    interference will the battle end.
    #       (Interference phase (perhaps where help may be negotiated if it's the main character's turn?)
    #        Update phase (if anything has changed, the monster's biases/strength may need to be updated))
    #   Until either:
    #      Victory phase:
    #        Final Interference Loop phase (maybe someone has the Trojan Horse?)
    #        Loot claim phase (character(s) get treasure and/or levels)
    #   or Running/defeat phase (character(s) try to run if possible, or are immediately caught)
    #        Final Interference Loop phase (maybe they've got Magic Lamp, or someone else wants to use Flask of Glue?)
    #        Bad Stuff phase (if unsuccessful at runaway)

#Starts the game.  Adds characters to the character list, prepares the decks,
# and gives the characters their starting supplies
def start_game(door_deck, treasure_deck):
    add_characters()
    make_battle_dict()
    door_deck, treasure_deck = create_decks()
    for character in character_list:
        get_supplies(character, door_deck, treasure_deck)

    
def take_turn(character, door_deck):
    opening_statement = input("\n").lower()
    if opening_statement == "open door":
        open_door(character, door_deck)


start_game(door_deck, treasure_deck)
turn = 0
turn_round = 1
while game_not_over:
    take_turn(character_list[turn], door_deck)
    turn = (turn+1)%(len(character_list))
    if turn == 0:
        turn_round += 1
