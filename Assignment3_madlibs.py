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

item = input("List an item from the supermarket: ")
item2 = input ("List an item from the supermarket: ")
Item3 = input ("List an item from the supermarket: ")


# Story

print(f"I went to shop and bought {item}")
print(f"I went to shop and bought {item}' and {item2}")
print(f"I went to shop and bought {item} and {item2} and {Item3}")

print("======================================")
print("I went to shop and bought " + item)
print("I went to shop and bought " + item + " and " + item2) 
print("I went to shop and bought " + item + " and " + item2 + " and " + Item3) 

