#!/usr/bin/python3
import random
import os

os.system('clear')

code = random.sample(range(0,9), 4)
bulls = 0
score = 0

print("Welcome to Cows and Bulls.\n")
print("I will choose a code of four numbers and you must guess the code.")
print("A cow indicates a number which is correct but in an incorrect place.")
print("A bull indicates a number which is correct and in a correct place.")
print("There are no duplicate numbers.")

while bulls < 4:

	cows = 0
	bulls = 0	

	guess_input = input("\nEnter four numbers: ")
	guess_list = list(guess_input)			# Convert string to list
	guess = list(map(int, guess_list))		# Convert string list to integer
	
	while len(guess) != 4:				# Check length validity of guess
		print("\nThat guess is invalid!")
		guess_input = input("\nEnter four numbers: ")
		guess_list = list(guess_input)		
		guess = list(map(int, guess_list))


	for i in range(len(code)):
		if guess[i] in code and guess[i] != code[i]:
			cows += 1
		if guess[i] in code and guess[i] == code[i]:
			bulls += 1

	print("\nCows:  ", cows)
	print("Bulls: ", bulls)
	score += 1

print("Congratulations! The code was", *code)
print("You took ", score, " attempts to crack the code")
