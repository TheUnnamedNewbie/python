#Number guess
#Joren Vaes

import random

#Generate random value, set maximum score, promt user for first guess.

value = random.randint(0,100)
score = float(25)
user = int(raw_input("Doe een gok! "))

#check if the users guess is within the boundaries (0>user>100), and asks for a new value untill it is within boundaries

while (user < 0 or user > 100):
	print user, " ligt niet binnen de grenswaarden (0 en 100). Doe een nieuwe gok! "
	user=int(raw_input())

#using while loop, promt the user for a new value untill the guess is right, unless the score is 0.
#in the while loop, use a if/else statement to display lower or higher
#if the value equals the generated value, or the score is 0
#the progran will check the score, and if it is not 0, display the value and score with a "succes"
#message. Else the program will tell the user he is out of tries.

while (user != value and int(score)>0):
	score = score/2
	if user < value:
		print"Te laag!",
	else:
		print"Te hoog!",
	user = int(input("Probeer nogeens! "))
else:
	score=int(score)	
	if score>0:
		print("Correct! ", value, "was de gezochte waarde! Je score is ", score)
	else:
		print("Je kansen zijn op! YOU FAILED!!! \n De gezochte waarde was ", value)




