from map import rooms
from player import * 
from items import *
from gameparser import *

#http://www.pygame.org/docs/ref/music.html
from os import system
import time
import string 

'''  TOD - made changes in list_of_items
           added 3 variabls in player.py
           added one line execute_use
           added the check_win_condition function
           imported string
           accidently deleted the import.pygame.music line sorry.'''


#Creates a string of items separated by commas
"Changes made here - Jacob"
def list_of_items(items):
    names = []
    for x in items:
        names.append(x['name'])
    return ', '.join(names)
    '''item_string = ""
    for item in items:
        item_string += (item["name"])
        if items.index(item) != len(items) - 1:
            item_string += ", "
    return item_string '''

#Prints a list of the items found in the specified room
def print_room_items(room):
    if room["items"]:
        print("There is " + list_of_items(room["items"]) + " here.\n")

#Prints a list of items in the player's inventory
def print_inventory_items(items):
    if inventory:
        print("You have " + list_of_items(inventory) + ".\n")

#Prints information about the specified room
def print_room(room):
    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()
    print_room_items(room)

#Retuns the room the current room exits into in a specified direction
def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]

#Prints a list of exits
def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")

#Prints the menu
def print_menu(exits, room_items, inv_items):
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        print("TAKE " + item["id"].upper() + " to take " + item["name"])
    for item in inv_items:
        print("DROP " + item["id"].upper() + " to drop your " + item["name"])
    for item in inv_items:
        print ("USE " + item["id"].upper() + " to use your " + item["name"])
    print()    
    print("What would you like to do?")

#Moves the player to the room they have chosen
"Changes made here, eliminates need for 'is_valid_exit' function - Jacob"
def execute_go(direction):
    global current_room
    exits = current_room["exits"]
    if direction in exits.keys():
        current_room = rooms[exits[direction]]
    else:
        print("\nYou cannot go there.")
        input()

#Picks up the item the player takes
def execute_take(item_id):
    item_in_list = False
    for item in current_room["items"]:
        if item_id in item["id"]:
            item_in_list = True
            if item_in_list:
                inventory.append(item)
                current_room["items"].remove(item)
                print("You have taken " + item["name"])
        else:
            print("You cannot take that.")
            input()

#Drops the item the player drops
"Changes made here - Jacob"
def execute_drop(item_id):
    item_in_list = False
    for item in inventory:
        if item_id == item["id"]:
            item_in_list = True
            current_room["items"].append(inventory.pop(inventory.index(item)))
    if item_in_list == False:
        print("You cannot drop that.")
        input()

#Uses the item the player specifies
"Changes made here - Jacob"
def execute_use(item_id):
    item_in_list = False
    for item in inventory:
        if item_id == item["id"]:
            item_in_list = True
            list_abilities(item)
    if item_in_list == False:
        print("You cannot use that.")

def list_abilities(item):
    print()
    print("How would you like to use the " + item["id"] + "?")
    print()
    for key in item["abilities"]:
        print(key + ": " + str(item["abilities"][key]))
    input("> ")

def check_win_condition(item):
    if current_room['name'] == 'Your bedroom' and item == 'rope':
        can_escape = True
    if bribed_sister == True:
        can_escape = True

#Executes the required function based on the command the player gives
def execute_command(command):
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1])
        else:
            print("Use what?")

    else:
        print("This makes no sense.")

#Prints the menu and takes the user input
def menu(exits, room_items, inv_items):
    print_menu(exits, room_items, inv_items)
    user_input = input("> ")
    normalised_user_input = normalise_input(user_input)
    return normalised_user_input

#Main game loop
def main():
    global can_escape
    print("""
 ____  ____  ____  __   _  _ /___    ____  ___   ___    __    ____  ____ 
(  _ \(_  _)(_  _)(  ) ( \/ )/ __)  ( ___)/ __) / __)  /__\  (  _ \( ___)
 ) _ < _)(_  _)(_  )(__ \  / \__ \   )__) \__ \( (__  /(__)\  )___/ )__) 
(____/(____)(____)(____)(__) (___/  (____)(___/ \___)(__)(__)(__)  (____)

""")
    print("There is a legendary house party tonight but your parents won't let you go.\nYou have to gather your things and sneak out of the house without your parents noticing.\nGood luck.")
    while True:
        print_room(current_room)
        print_inventory_items(inventory)
        command = menu(current_room["exits"], current_room["items"], inventory)
        execute_command(command)
        system('cls')
        if can_escape == True:
            print('Woohoo /some other text/')
            break

if __name__ == "__main__":
    main()
