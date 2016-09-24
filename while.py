#!/usr/bin/python

# while loop

from random import random

num = int(random()*100)

while True:
	guess = int(input("Enter a number: "))
	if num == guess:
		print("You nailed the quiz. The number is {}".format(num))
		break

	if guess > num:
		print("Try with smaller number...")
	elif guess < num:
		print("Try with larger number...")