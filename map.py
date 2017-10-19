from items import *
'''
room_reception = {
    "name": "Reception",

    "description":
    """You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west.""",

    "exits": {"south": "Admins", "east": "Tutor", "west": "Parking"},

    "items": [item_biscuits, item_handbook]
}
'''
room_bedroom = {
    "name" : "Your Bedroom",

    "description" : "",

    "exits" : {"out" : "U_Hallway"},

    "items" : [item_laptop]
}

room_lounge = {
    "name" : "Lounge",

    "description" : "",

    "exits" : {"hallway" : "D_Hallway", "kitchen" : "Kitchen"},

    "items" : []
}

room_upstairs_hallway = {
    "name" : "Upstairs Hallway",

    "description" : "",

    "exits" : {"" : "Bedroom", "" : "P_Bedroom", "" : "S_Bedroom", "" : "Closet", "" : "Bathroom", "downstairs" : "D_Hallway"},

    "items" : []
}

room_closet = {
    "name" : "Closet",

    "description" : "",

    "exits" : {"out" : "U_Hallway"},

    "items" : [item_backpack, item_flashlight]
}

room_kitchen = {
    "name" : "Kitchen",

    "description" : "",

    "exits" : {"lounge" : "Lounge"},

    "items" : [item_lighter, item_coke, item_vodka]
}

room_bathroom = {
    "name" : "Bathroom",

    "description" : "",

    "exits" : {"out" : "U_Hallway"},

    "items" : [],
}
room_downstairs_hallway = {
    "name" : "Downstairs Hallway",

    "description" : "",

    "exits" : {"lounge" : "Lounge", "downstairs" : "Basement", "upstairs" : "U_Hallway"},

    "items" : [],
}
room_parent_bedroom = {
    "name" : "Parent's Bedroom",

    "description" : "",

    "exits" : {"out" : "U_Hallway"},

    "items" : [],
}
room_sharon_bedroom = {
    "name" : "Sharon's Bedroom",

    "description" : "",

    "exits" : {"out" : "U_Hallway"},

    "items" : [],
}
room_basement = {
    "name" : "Basement",

    "description" : "",

    "exits" : {"upstairs" : "D_Hallway"},

    "items" : [item_rope]
}
rooms = {
    "B_Bedroom" : room_bedroom,
    "P_Bedroom" : room_parent_bedroom,
    "S_Bedroom" : room_sharon_bedroom,
    "Lounge" : room_lounge,
    "D_Hallway" : room_downstairs_hallway,
    "U_Hallway" : room_upstairs_hallway,
    "Closet" : room_closet,
    "Kitchen" : room_kitchen,
    "Bathroom" : room_bathroom,
    "Basement" : room_basement
}
