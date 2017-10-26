from map import rooms
from player import * 
from items import *
from gameparser import *
import math
import msvcrt
import time
import timer
import winsound
from spiderfight import *
from os import system

#Creates a string of items separated by commas
"Changes made here - Jacob"
def list_of_items(items):
    names = []
    for x in items:
        names.append(x['name'])
    return ', '.join(names)

#Prints a list of the items found in the specified room
def print_room_items(room):
    if room["items"]:
        print("There is " + list_of_items(room["items"]) + " here.\n")
        for item in room["items"]:
	        print ("! " + item["description"] + " !")

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
    print()

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
    for item in current_room["items"]:
        if item_id == item["id"]:
            inventory.append(item)
            current_room["items"].remove(item)
            print("You have taken " + item["name"])
            return
    print("You cannot take that.")
    input()

#Drops the item the player drops
"Changes made here - Jacob"
def execute_drop(item_id):
    for item in inventory:
        if item_id == item["id"]:
            current_room["items"].append(inventory.pop(inventory.index(item)))
            if item_id == "rope":
                del rooms["B_Bedroom"]["exits"]["window"]
            elif item_id == "flamethrower":
                del rooms["D_Hallway"]["exits"]["basement"]
            return
    print("You cannot drop that.")
    input()

#Uses the item the player specifies.
"Changes made here - Jacob"
def execute_use(item_id):
    item_in_list = False
    for item in inventory:
        if item_id == item["id"]:
            item_in_list = True
            if item_id == "watch":
                view_watch()
            else:
                list_abilities(item)
    if item_in_list == False:
        print("You cannot use that.")
        input()

#Lists the abilities of a given item.
def list_abilities(item):
    item_abilities = item["abilities"]
    if len(item_abilities) >= 1:
        print()
        print("How would you like to use the " + item["id"] + "?")
        print()
        for key in item_abilities:
            if key != "merge":
                print(key + ": " + str(item_abilities[key]))
        print()
        print("Enter 'MERGE' to view items to merge.")
        print()
        print("Enter 'BACK' to go back to the main menu:")
        print()
        user_input = normalise_input(input("> "))
        if user_input[0] == "merge":
            special_use_list = list(item_abilities["merge"].keys())
            counter = list_choices(special_use_list)
            choice = ""
            #Validation check for numerical input
            while choice.isdigit() is False:
                choice = input("> ")
                if choice.isdigit() is False:
                    print("Please enter a valid option.\n")
            choice = int(choice)
            if choice >= counter:
                return
            merge_items(special_use_list[choice - 1], item_abilities["merge"])
        elif user_input[0] == "menu":
            return
    else:
        print("This item currently has no use.\n")
                              
def list_choices(uses):
    i = 1
    for item in uses:
        if get_inv_item(item) in inventory:
            print()
            print(str(uses.index(item) + 1) + ": merge with " + item + ".")
            i += 1
    print()
    print(str(i) + ": to return to the menu.")
    print()
    return i
def get_inv_item(item_id):
    for item in inventory:
        if item_id == item["id"]:
            return item
    
#Used to merge two items together to create a new item.
def merge_items(item, abilities):
    if item in abilities and get_inv_item(item) in inventory:
        new_item = abilities[item]
        if new_item not in inventory:
            print()
            print("You now have a " + new_item["id"] + ".")
            input()
            inventory.append(new_item)
        else:
            print()
            print("You already have a " + new_item["id"] + ".")
            input()
    if get_inv_item(item) not in inventory:
        print("\nYou must first find this item before you can merge it.\n")
        
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

def view_watch():
    system('cls')
    mins = math.floor(10 - ((time.time() - start) / 60))
    secs = math.floor(60 - (time.time() - start) % 60)
    timer.countdown(mins, secs)

#Prints the menu and takes the user input
def menu(exits, room_items, inv_items):
    print_menu(exits, room_items, inv_items)
    user_input = input("> ")
    normalised_user_input = normalise_input(user_input)
    return normalised_user_input

def add_room(item, room, new_room):
    if item in inventory:
        room["exits"][new_room] = rooms[new_room]["name"]

def initiate_fight():
    if current_room["name"] == "basement":
        spider_web_fight()
        

#Main game loop
def main():
    print("""
 ____  ____  ____  __   _  _ /___    ____  ___   ___    __    ____  ____ 
(  _ \(_  _)(_  _)(  ) ( \/ )/ __)  ( ___)/ __) / __)  /__\  (  _ \( ___)
 ) _ < _)(_  _)(_  )(__ \  / \__ \   )__) \__ \( (__  /(__)\  )___/ )__) 
(____/(____)(____)(____)(__) (___/  (____)(___/ \___)(__)(__)(__)  (____)

""")
    print("There is a legendary house party tonight but your parents won't let you go.\nYou have to gather your things and sneak out of the house without your parents noticing.\nGood luck.")
    global start
    start = time.time()
    bg_music_playing = False
    while time.time() - start < 600 and current_room["name"] != "window":
        if current_room["name"] == "Basement":
            winsound.PlaySound("sounds/basement.wav", winsound.SND_LOOP|winsound.SND_ASYNC)
            bg_music_playing = False
        elif current_room["name"] == "Bathroom":
            winsound.PlaySound("sounds/bathroom.wav", winsound.SND_LOOP|winsound.SND_ASYNC)
            bg_music_playing = False
        elif bg_music_playing == False:
            winsound.PlaySound("sounds/bgmusic.wav", winsound.SND_LOOP|winsound.SND_ASYNC)
            bg_music_playing = True
        add_room(item_rope, rooms["B_Bedroom"], "window")
        add_room(item_flamethrower, rooms["D_Hallway"], "basement")
        print_room(current_room)
        print_inventory_items(inventory)
        command = menu(current_room["exits"], current_room["items"], inventory)
        execute_command(command)
        initiate_fight()
        system("cls")
    if current_room["name"] == "window":
        winsound.PlaySound("sounds/window.wav")
        print("Congratulations, you won!")
        input()
    else:
        print("You ran out of time")
        input()
if __name__ == "__main__":
    main()
