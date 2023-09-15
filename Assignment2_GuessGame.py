"""
Project Brief
This project uses the random module in Python. The program will first randomly generate a
number unknown to the user. The user needs to guess what that number is. (In other words, the
user needs to be able to input information.) If the user’s guess is wrong, the program should
return some sort of indication as to how wrong (e.g. The number is too high or too low). If the
user guesses correctly, a positive indication should appear. You’ll need functions to check if the
user input is an actual number, to see the difference between the inputted number and the
randomly generated numbers, and to then compare the numbers.
Concepts to keep in mind:
● Random function
● Variables
● Integers
● Input/Output
● Print
● While loops
● If/Else statements

"""

import random

minValue = 1
maxValue = 100

randomValue = random.randint(minValue, maxValue)

#update values here if changes needed

userGuess = 'wrong'

while userGuess == 'wrong':

    attempt = input(f"Guess the number I'm thinking of between {minValue} and {maxValue}: ")

    try:
         #make sure user input is a number
         number = int(attempt)

         if number == randomValue:
            print("Wow! You're a genius!")
            userGuess = 'right'
         elif number > randomValue:
             print("No, go lower. Guess again")
         elif number < randomValue:
             print("No, go higher. Guess again")
    except ValueError:
         print("I said guess a number!")