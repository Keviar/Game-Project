from items import *
from map import rooms

#Player's inventory of items.
inventory = [item_keys, item_watch]

#Room the player starts in.
current_room = rooms["B_Bedroom"]

#Defines how many items Bill can see varying on their size and the light
#intensity in the room.
vision = 20
