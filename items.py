item_vodka = {
    "id" : "vodka",

    "name" : "bottle of Vodka",

    "description": "Not your favorite drink, but it's about as much alcohol as you can fit in one bottle. You'll impress with this that's for sure. It just needs something to mix it with.",

    "abilities" : {}
}

item_coke = {
    "id" : "coke",

    "name" : "bottle of Coke",

    "description" : "The sugary goodness that everybody loves, nobody is going to notice this bottle missing. All you need is a spirit and you're set for the party. Well, as far as drinks go. ",

    "abilities" : {}
}

item_backpack = {
    "id" : "backpack",

    "name" : "backpack",

    "description" : "Your old school rucksack, you haven't seen this thing since year 7. You thought it was cool but nobody else did. This will help you to carry the things you need to escape.",

    "abilities" : {}
}

item_keys = {
    "id" : "keys",

    "name" : "set of keys",

    "description" : "Keys to your house. Make sure you don't lose them or else you'll be sleeping on the streets tonight.",

    "abilities" : {}
}

item_rope = {
    "id" : "rope",

    "name" : "rope",

    "description" : "An old but strong rope. This sinews got a date with a window, and you've got a date with a party.",

    "abilities" : {}
}

item_laptop = {
    "id" : "laptop",

    "name" : "laptop",

    "description" : "You can't bring your music along without this.",

    "abilities" : {}
}

item_flashlight = {
    "id" : "flashlight",

    "name" : "flashlight",

    "description" : "How else are you going to venture into dark and scary places?",

    "abilities" : {}
}

item_flamethrower = {
    "id" : "flamethrower",

    "name" : "flamethrower",

    "description" : "Just like you saw your mate John do out the back of the school shed, who knew deodeorant could be so fun?! Flamethrower is an understatement.",
    
    "abilities" : {}
}

item_lighter = {
    "id" : "lighter",

    "name" : "lighter",

    "description" : "You don't smoke, that would just be silly. But a bit of deodeorant and this might help you get through that basement!",

    "abilities" : {"merge" : {"deodorant" : item_flamethrower}}
}

item_deodorant = {
    "id" : "deodorant",

    "name" : "deodorant",

    "description" : "You smell fine, but you can't help but notice the big flammable icon on the can.",

    "abilities" : {"merge" : {"lighter" : item_flamethrower}}
}

item_glasses = {
    "id" : "glasses",

    "name" : "pair of glasses",

    "description" : "You weren't gifted with the best eyesight. But thanks to these you can actually see.",

    "abilities" : {}
}

item_watch = {
    "id" : "watch",

    "name" : "watch",

    "description" : "Would you look at the time! Time to get to the party. Better not take too long trying to get there.",

    "abilities" : {}
}
