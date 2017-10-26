from items import *

room_bedroom = {
    "name" : "Your Bedroom",

    "description" : ["""
You stand in your bedroom. The room is traditional of any teenage boy's bedroom. A poster from your 
favourite band, Muse, overlooks your single bed. Your desk sits next to the window, on it, a few 
knick-knacks and your computer. The door is open and faces the dimly lit upstairs hallway. You look at 
your window, could you get out here? Maybe, but it'd be a long drop.""" ,
"""
You stand idly glaring into your bedroom, the wind blows through the curtains as you pan 
the room. Your bed is covered by a generic blue duvet cover, your Mum wouldn't let you have 
the cool one. Overlooking it, a Muse poster, your favourite band. You glare across to your 
desk, your computer hums gently with a dimly lit screen. Did you leave it on again? The door 
is behind you and you hear faint sounds coming from the upstairs hallway. As the wind continues 
to sweep through your room you consider the possibility of climbing out of the window. If only 
it wasn't so high up, you definitely couldn't jump out safely. But maybe you could use something to get down?""",
"""
You're in your bedroom. The floor is a mess, reminding you of your Mum asking you to clean 
it earlier, it'll have to wait. You stare fondly at your rock poster, the room's best feature. 
Your unmade bed only adds to the teenage chaos. From the corner your computer is whirring away quietly. 
The door is open and you can see out into the upstairs hallway. Near your bed you spot your window. 
It's partially open, luckily you know it opens much more than that. Could you get out here? 
There's no way you'd survive the drop without at least broken ankles."""],
    
    "exits" : {"out" : "U_Hallway"},

    "items" : [item_laptop, item_glasses]
}

room_window = {
    "name" : "window",

    "description" : ["Freedom"],

    "items" : "",

    "exits" : ""
}

room_lounge = {
    "name" : "Lounge",

    "description" : ["""
You stand in the lounge quietly, your parents glare at you briefly but seem to be lost in the TV show. 
You'd need to pass them to go to the kitchen. The walls are decorated with your Mum's favourite art. 
In the corner you see Dad's dusty collection of old magazines, you swear Mum told him to throw those out. 
As the TV blares The One Show, your mind wanders to the kitchen again. 
You can't go to a party without some alcohol, your best bet is to check in there.""",
"""
You enter the lounge, trying not to make a sound. Your parents look up from The One Show blaring out of the TV, 
but it soon gains their attention again. You look at the art on the walls, you still don't know why 
your Mum likes that artist so much, just a bunch of squiggles. You see the door to the kitchen in the corner, 
nobody likes turning up to a party without drinks and you're pretty sure the good stuff's in there. 
The dog's sleeping in his bed, where did that mutt get to?""",
"""
You creep into the lounge, trying to stop the door from creaking too much. 
The lights are turned down low and you catch a glimpse of the One Show. 
Your parents briefly look your way but are soon distracted by the TV again. 
The kitchen light is on and shines through into the room, you're going to need 
drink for this party and you bet you will find it in there."""],

    "exits" : {"hallway" : "D_Hallway", "kitchen" : "Kitchen"},

    "items" : []
}

room_upstairs_hallway = {
    "name" : "Upstairs Hallway",

    "description" : ["""
You find yourself standing in the middle of the upstairs hallway, you can access all of 
the upstairs rooms from here. The carpet is old and tired, and a washing basket sits by the stairs. 
You could go downstairs or keep exploring the rooms upstairs. You swear you can hear Sharon singing,
it doesn't sound good.""",
"""
You're in the upstairs hallway, you see doors to various rooms spread around you. 
You stand on the old beige carpet and think about what you're going to do next. 
You could explore up here, or head downstairs. The overhead light flickers as you decide, 
you thought Dad was supposed to fix that?""",
"""
The upstairs hallway never looked so plain, the old beige carpet definitely needs changing. 
The washing basket sits on its own by the stairs, it's overflowing with everybody's clothes. 
You contemplate either looking around upstairs or taking your chances downstairs. 
You need to get out of the house, and fast."""],

    "exits" : {"1" : "B_Bedroom", "2" : "P_Bedroom", "3" : "S_Bedroom", "4" : "Closet", "5" : "Bathroom", "downstairs" : "D_Hallway"},

    "items" : []
}

room_closet = {
    "name" : "Closet",

    "description" : ["""
You squeeze into the upstairs closet, making room for yourself between the old coats and forgotten shoes. 
You feel perfectly hidden here. You're sure if you look around hard enough you'll find something useful. 
You don't want to stay too long though, you'll miss your party!""",
"""
You push your way into the upstairs closet, sliding yourself between the old coats and forgotten footwear. 
Nobody goes in this closet much, but there are probably a few handy things in here. 
Everybody's always throwing stuff in here. Better not stay too long, the party won't wait forever.""",
"""
After opening the door you make your way into the cramped upstairs closet, finding yourself lost in-between 
old shoes and some dusty coats. Peering around you see the floor is also occupied with random items that 
have been thrown in here over time. You're sure you could find something useful between them all. 
You don't think staying here is a good idea, you've got an escape to prepare!"""],

    "exits" : {"out" : "U_Hallway"},

    "items" : [item_backpack, item_flashlight]
}

room_kitchen = {
    "name" : "Kitchen",

    "description" : ["""
Few, you made it past your parents without them asking questions. 
You've just had dinner and going into the kitchen too much is going to look suspicious. 
You look across the counters and see an assortment of kitchen utensils. 
The lights in here are bright and you catch your own reflection in the window. 
The fridge sits in the corner of the room, you could always check in there for drinks. 
You might even be able to find something useful in the draws. The only way out is back through the lounge.""",
"""
You squeeze past your parents into the kitchen, it doesn't look like you raised too much suspicion. 
You could just be getting a glass of water right? There's some washing up draining next to the 
kitchen sink, and various utensils are scattered across the worktop. The fridge looms ominously 
in the corner, could you find something in there? Or maybe you should check the draws. 
If you want to leave it's going to have to be through the lounge.""",
"""
Your parents didn't really look up when you went into the kitchen, hopefully they don't suspect anything. 
They're going to be expecting to be in bed soon. Better get everything ready for the party soon. 
You look across the brightly lit kitchen, it somewhat resembles a generic 1950's kitchen, 
the black and white tiles definitely add to the effect. The fridge is in the corner, 
you might be able to find something for the party in there or maybe try the kitchen draws. 
If you want to leave it's going to have to be back through the lounge, quietly."""],

    "exits" : {"lounge" : "Lounge"},

    "items" : [item_lighter, item_coke, item_vodka]
}

room_bathroom = {
    "name" : "Bathroom",

    "description" : ["""
You enter the brightly lit bathroom, splayed around the place are vague items all relating to the ocean. The tiles are blue and the walls are
painted to mimic the style of a lighthouse. You've never even been to the sea but your Mum loves the seaside look. Nobody's going to look for 
you in here. """,
                 """
You lock the door as you enter the bathroom, no one's going to bother you in here. The seaside theme of the room makes your stomach churn,
it's a bit much, even for you. The blue tiles and lighthouse themed walls stare back at you whilst you decide on what to do, you've never
even been to the sea.""",
                 """
You go into the bathroom and glare across the room. A few years back your Mum decided to retheme it, it now resembles a cheap beachside shop.
The floor is covered in bright blue tiles and the walls are coloured as to resemble a lighthouse. As bad as the decor is, you know nobody is
going to bug you in here."""],

    "exits" : {"out" : "U_Hallway"},

    "items" : [],
}
room_downstairs_hallway = {
    "name" : "Downstairs Hallway",

    "description" : ["""
You stand at the bottom of the stairs in your downstairs hallway. 
The decor is plain and a fixture hangs from the ceiling, spreading light across the room. 
You see the front door, there's no way you're opening that without your parents noticing. 
You look up the stairs and see the landing, equally as dull. You think about your next steps, 
should you explore the rooms down here or maybe venture into the basement?""",
"""
You find yourself standing in your downstairs hallway, you feel a slight gust of wind 
coming from the front door. There's no way you're getting out there without your parents knowing. 
You could waste more time in this rather plain room, or you could explore the rooms around you, 
maybe even head upstairs. You also see the entrance to the basement, are you brave enough for that? 
You can't remember the last time anyone went down there.""",
"""
You look around, the downstairs hallway. Nothing here looks interesting, 
other than your potential to explore the house. The front door tempts you 
with its quit exit potential, but there's not a chance you'd get away with that.
After all your parents notice for sure. The entrance to the basement 
greets you eerily, should you check down there? You can't remember the last time 
someone actually went down there. Whatever you do, you should probably do it quickly. 
When did you last check your watch?"""],

    "exits" : {"lounge" : "Lounge", "downstairs" : "U_Hallway"},

    "items" : [],
}
room_parent_bedroom = {
    "name" : "Parent's Bedroom",

    "description" : ["""
You sneak into your parent’s bedroom, the number of pillows on the bed astounds you.
I don't know if you're going to find anything good in here and you're probably going 
to get in trouble for trying. Maybe you should leave.""",
"""
You creep quietly into your parent’s bedroom, it's lit dimly by a wall lamp in the corner. 
You don't see anything interesting here, unless you're planning to go to the party in one of your Dad's suits.
Getting out of here sounds good about now.""",
"""
You gently push the door to your parent's bedroom open, it looks alien to you
with its adult decorations and assortment of pillows. After briefly looking across 
the room you decide nothing of interest is here. You better get out before you get caught."""],

    "exits" : {"out" : "U_Hallway"},

    "items" : [],
}
room_sharon_bedroom = {
    "name" : "Sharon's Bedroom",

    "description" : ["""
You take a deep breath and go into your sister's bedroom. You're pretty sure if 
she saw you in here she'd kill you. Sharon isn't someone you want to mess with. 
The room's offensive pink walls hurt your eyes, you're not going to find anything for the party here.
A thought suddenly crosses your mind, maybe Sharon could help you escape? 
You'd have to make it worth her while though.""",
"""
You stand at the entrance to Sharon's room and peer in, seeing only a grotesque 
pink hue emanating from the walls. It's almost as messy as yours, you never hear
Mum complaining about her room. You don't think there's anything worth bringing 
to the party here, but maybe Sharon could help you escape? She definitely wouldn't do it for free though.""",
"""
You can't believe you're actually going into Sharon's bedroom, you wimp out 
at the entrance deciding only to look in. The room is painted a horrific pink, 
Sharon's signature colour. You decide quickly that you don't see anything of interest, but while you're here
you can't help but think that Sharon might be able to help you escape, 
she definitely wouldn't help without some sort of bribe. Even worse, she might decide to snitch on you."""],

    "exits" : {"out" : "U_Hallway"},

    "items" : [],
}
room_basement = {
    "name" : "basement",

    "description" : ["""
You step down into the basement, almost slipping on the old wooden stairs.
A solemn drawstring meets your gaze and as you pull it the room is barely 
illuminated by an old fashioned lightbulbs. Everywhere you look you see cobwebs, 
people really haven't been down here for a long time. You're sure you'll find 
something useful down here, but it's not too late to go back.""",
"""
You stumble down the old wooden stairs, it looks exactly like a horror movie down here. 
Hopefully that's all the basement has in similar with a horror movie. 
You turn on the old light, it struggles to light even the smallest corner of the room. 
All you can see from here arecobwebs, did that giant spider from Skyrim move in here or something? 
It's not too late for you to turn back. But inside you know you're going to need whatever you can find in here.""",
"""
You take your first step down into the basement, a loud creak greets your approach. 
You fumble down and reach the light switch. A tired lightbulb splutters into action, 
barely illuminating even the stairs. Everywhere you look you see cobwebs, yikes. You have a strong
feeling you're going to need whatever's down here. It's not too late to go back."""],

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
