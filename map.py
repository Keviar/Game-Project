from items import *

room_bedroom = {
    "name" : "Your Bedroom",

    "description" : "You are now in your bedroom where your parents expect you to be studying tonight.",

    "exits" : {"out" : "U_Hallway"},

    "items" : [item_laptop, item_glasses]
}

room_lounge = {
    "name" : "Lounge",

    "description" : "This is where your parents spend most of their time watching TV.",

    "exits" : {"hallway" : "D_Hallway", "kitchen" : "Kitchen"},

    "items" : []
}

room_upstairs_hallway = {
    "name" : "Upstairs Hallway",

    "description" : "",

    "exits" : {"bedroom1" : "B_Bedroom", "beedroom2" : "P_Bedroom", "bedroom3" : "S_Bedroom", "closet" : "Closet", "bathroom" : "Bathroom", "downstairs" : "D_Hallway"},

    "items" : []
}

room_closet = {
    "name" : "Closet",

    "description" : "You can use this room to hide!",

    "exits" : {"out" : "U_Hallway"},

    "items" : [item_backpack, item_flashlight]
}

room_kitchen = {
    "name" : "Kitchen",

    "description" : "You are now in the kitchen where you can collect items from the fridge and counter.",

    "exits" : {"lounge" : "Lounge"},

    "items" : [item_lighter, item_coke, item_vodka]
}

room_bathroom = {
    "name" : "Bathroom",

    "description" : "You can hide here!",

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

    "description" : "Maybe not the best place to hide.",

    "exits" : {"out" : "U_Hallway"},

    "items" : [],
}
room_sharon_bedroom = {
    "name" : "Sharon's Bedroom",

    "description" : "Your sisters bedroom, she's very nosey and may ruin your escape so watch out!",

    "exits" : {"out" : "U_Hallway"},

    "items" : [],
}
room_basement = {
    "name" : "Basement",

    "description" : "You are now in the basement, there are a lot of cob webs here and it's difficult to see without a light.",

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
