#Random Number Guesser

import random

print("Welcome to the Random Number Guesser!")

random_number = random.randint(1,100) # 1 <= N <= 100

guess = None #the users current guess
attempts = 0 #attempts the user has made
guessed = False

while(not guessed):
	guess = input("Please enter a guess between 1 and 100: ")

	if guess.isdigit():

		guess = int(guess)

		if guess > random_number:
			print("Guess is too high!")
		elif guess < random_number:
			print("Guess is too low!")
		else:
			guessed = True

		attempts += 1

	else:
		print("Invalid input, please try again.")

#the while loop stopped running 

print("You guessed it!\nIt took you",attempts,"attempts to guess",random_number)







