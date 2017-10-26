import time
import random
import winsound
from os import system

def spider_web_fight():
	system('cls')
	basement = ['window', 'cellar', 'door', 'control room']
	direction = ['front', 'left', 'back', 'right']
	print("You must burn the spider webs before the timer runs out!")
	time.sleep(3)
	print("You must type the direction the web is at! Every time you destroy a web, you face at the location the web was at.")
	time.sleep(3)
	print("Memorize the room! If you forget where you are facing, you can check where everything is located by typing check.")
	time.sleep(3)
	for y in range (0, 4):
		print ("The " + basement[y] + " is at the " + direction[y] + ".")
	time.sleep(7)
	print ("You have 30 seconds, Go!")
	time.sleep(1)
	i=0
	win_fight = False
	win_fight2=False
	start_fight=time.time()
	counter=0
	while (win_fight==False):
		m = random.randint(0,3)
		print ("There is a spider web at the " + basement[m] + "!")
		current_web=basement[m]
		l = input("> ")
		if l == 'check':
			for x in range (0, 4):
				if i==4:
					i=0
				print ("The " + basement[i] + " is at the " + direction[x] + ".")
				i = i+1
			current_time=30-int(time.time()-start_fight)
			print("You have ", current_time, " seconds left!")
			print ("")
			time.sleep(1)
		else:
			if l == 'front':
				i = i+0
			if l == 'left':
				i = i+1
			if l == 'back':
				i = i+2
			if l == 'right':
				i = i+3
			if (i>=4):
				i=i-4	
			if (basement[i]==current_web):
				print("You burnt the web!")
				counter=counter+1
			else:
				print("You missed... do you even know where you are facing now!?")
		if counter>4:
			win_fight=True
		if (time.time()-start_fight>30):
			print("You are too slow.... the spider ate you.")
			break
	if win_fight==False:
		print("It's over.")
		time.sleep(2)
		return win_fight2
	print ("There is a spider web at.... you!?")
	time.sleep(3)
	print ("The spider attacks you!")
	time.sleep(1)
	print("""
		                            ____                      
          /---.'.__             ____//
               '--.\           /.---'
          _______  \\         //
        /.------.\  \|      .'/  ______
       //  ___  \ \ ||/|\  //  _/_----.\__
      |/  /.-.\  \ \:|< >|// _/.'..\   '--'
         //   \'. | \'.|.'/ /_/ /  \\
        //     \ \_\/" ' ~\-'.-'    \\
       //       '-._| :H: |'-.__     \\
      //           (/'==='\)'-._\     ||
      ||                        \\    \|
      ||                         \\    '
      |/                          \\
                                   ||
                                   ||
                                   \\
                                    '
                                    """)
	while (win_fight2==False):
		print("""
You can:
BURN the spider using your flamethrower
HIT the spider with your flamethrower
PET the spider to calm it down
RUN because your balls haven't dropped yet """)
		l=input("> ")
		if l=="burn":
			print("The spider is too agile for your flames... you missed!")
		if l=="hit":
			print("You managed to hit the spider!")
			print ("""
You can:
HIT it again!
BURN it now that it's slow!
PET its almost dead carcass
You cannot RUN... you're too deep in this """)
			p = input("> ")
			if p=="hit":
				print("Thousands of little spiderlings come out of the mother's dead body... and they're mad, it's all over")
				time.sleep(3)
				break
			if p=="burn":
				print("You burnt it! And the thousand little spiders that were in it! Thank god you didn't actually hit it again...")
				time.sleep(3)
				win_fight2=True
				break
			if p=="pet":
				print("What, you think now it will work all of a sudden?")
				time.sleep(2)
				print("The spider tries to bite you...")
				time.sleep(2)
				print("The spider bit you! It's over.")
				time.sleep(2)
				break
			else:
				print("The spider missed! Keep going.")
				time.sleep(2)
		if l=="pet":
			print("What are you, stupid?")
		if l=="run":
			print("Oh wow the door is magically locked while you're in this fight, WOW you can't run.")
		time.sleep(2)
		if win_fight2==False:
			print("The spider tries to bite you...")
			time.sleep(2)
			a=random.randint(0,2)
			if(a==0):
				print("The spider bit you! It's over.")
				time.sleep(2)
				break
			else:
				print("The spider missed! Keep going.")
				time.sleep(2)
	return win_fight2
