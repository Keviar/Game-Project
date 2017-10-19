from map import rooms
from player import * 
from items import *
from gameparser import *

#Creates a string of items separated by commas
def list_of_items(items):
    item_list = ""
    list_length = len(items)
    for item in items:
        item_list = item_list + item["name"]
        if list_length > 1:
            item_list = item_list + ", "
        list_length -= 1
    return item_list

#Prints a list of the items found in the specified room
def print_room_items(room):
    if len(room["items"]) > 0:
        print("There is " + str(list_of_items(room["items"]) + " here.\n"))

#Prints a list of items in the player's inventory
def print_inventory_items(items):
    print("You have " + str(list_of_items(inventory) + ".\n"))

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

    if len(room_items) > 0:
        for item in room_items:
            print("TAKE " + item["id"].upper() + " to take " + item["name"])
    if len(inv_items) > 0:
        for item in inv_items:
            print("DROP " + item["id"].upper() + " to drop your " + item["name"])
    
    print("What do you want to do?")

#Checks if a given exit is valid
def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits

#Moves the player to the room they have chosen
def execute_go(direction):
    global current_room
    if is_valid_exit(current_room["exits"], direction):
        current_room = rooms[current_room["exits"][direction]]
        print("Moving to " + current_room["name"])
    else:
        print("You cannot go there.")

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

#Drops the item the player drops
def execute_drop(item_id):
    item_in_list = False
    for item in inventory:
        if item_id in item["id"]:
            item_in_list = True
            current_room["items"].append(item)
            inventory.remove(item)
    if item_in_list == False:
        print("You cannot drop that.")

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
    while True:
        print_room(current_room)
        print_inventory_items(inventory)
        command = menu(current_room["exits"], current_room["items"], inventory)
        execute_command(command)

if __name__ == "__main__":
    main()