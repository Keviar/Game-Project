from items import *
from map import rooms

#Player's inventory of items.
inventory = [item_keys]

#Room the player starts in.
current_room = rooms["B_Bedroom"]

#Defines how many items Bill can see varying on their size and the light
#intensity in the room.
vision = 20

#See if he overheard his parents who are in the lounge
sister_weakspot = False
#See if he bribed his sister
sister_bribed = False
#see if all the conditions are met
can_escape = False
