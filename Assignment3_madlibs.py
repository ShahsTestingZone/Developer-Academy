"""
Project Brief
Inspired by Summer Son’s Mad Libs project with Javascript. The program will first prompt the
user for a series of inputs a la Mad Libs. For example, a singular noun, an adjective, etc. Then,
once all the information has been inputted, the program will take that data and place them into a
premade story template. You’ll need prompts for user input, and to then print out the full story at
the end with the input included.
Concepts to keep in mind:
● Strings
● Variables
● Concatenation
● Print
Deliverables
A pretty fun beginning project that gets you thinking about how to manipulate user inputted data.
Compared to the prior projects, this project focuses far more on strings and concatenating.
Have some fun coming up with some wacky stories for this!

"""

#Input

color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
blank= input("Complete the sentence: 'Me + xxx = Us: ")

print("=====================================")
print("Roses are " + color)
print( plural_noun + " are blue")
print ("This assignment is created for " + blank)
print("=======================================")

# Our code is open-source, please let us know how you would like to improve it.
# Contribute to out team through patreon or paypal 

#Suggestions
# Add while loop to continue playing game
# Make sure inputs are not digits
# Extend Poem
# Add function to check that words in the game are not repeated, if in a loop
# Adapt the game to be similar to cards of humanity
