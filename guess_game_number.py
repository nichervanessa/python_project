#Guess Game we can select number randomly
import random

number_var=random.randrange(1,100)
guess_var=int(input("Enter any Number That You want"))
#
while number_var!= guess_var:
	if guess_var <number_var:
		print("Too low")
		guess_var=int(input("Enter another Number:"))
	elif guess_var>number_var:
		print("Too Hight")
		guess_var=int(input("Enter Number again:"))

	else:
		break
print("You Guessed it right")
