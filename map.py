from items import *

room_bedroom = {
    "name" : "Your Bedroom",

    "description" : "",

    "exits" : {"out" : "U_Hallway"},

    "items" : [item_laptop, item_glasses]
}

room_window = {
    "name" : "window",

    "description" : "Freedom",

    "items" : "",

    "exits" : ""
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

    "exits" : {"1" : "B_Bedroom", "2" : "P_Bedroom", "3" : "S_Bedroom", "4" : "Closet", "5" : "Bathroom", "downstairs" : "D_Hallway"},

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

    "exits" : {"lounge" : "Lounge", "upstairs" : "U_Hallway"},

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
    "name" : "basement",

    "description" : "",

    "exits" : {"upstairs" : "D_Hallway"},

    "items" : [item_rope]
}
rooms = {
    "B_Bedroom" : room_bedroom,
    "window" : room_window,
    "P_Bedroom" : room_parent_bedroom,
    "S_Bedroom" : room_sharon_bedroom,
    "Lounge" : room_lounge,
    "D_Hallway" : room_downstairs_hallway,
    "U_Hallway" : room_upstairs_hallway,
    "Closet" : room_closet,
    "Kitchen" : room_kitchen,
    "Bathroom" : room_bathroom,
    "basement" : room_basement
}
