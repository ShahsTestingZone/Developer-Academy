"""
Project Brief

Remember Adventure? Well, we’re going to build a more basic version of that. A complete text
game, the program will let users move through rooms based on user input and get descriptions
of each room. To create this, you’ll need to establish the direction in which the user can move, a
way to track how far the user has moved (and therefore which room he/she is in), and to print
out a description. You’ll also need to set limits for how far the user can move. In other words,
create “walls” around the rooms that tell the user, “You can’t move further in this direction.”

Concepts to keep in mind:
● Strings
● Variables
● Input/Output
● If/Else Statements
● Print
● List
● Integers

Deliverables
The tricky parts here will involve setting up the directions and keeping track of just how far the
user has “walked” in the game. I suggest sticking to just a few basic descriptions or rooms,
perhaps 6 at most. This project also continues to build on using user inputted data. It can be a
relatively basic game, but if you want to build this into a vast, complex word, the coding will get
substantially harder, especially if you want your user to start interacting with actual objects
within the game. That complexity could be great, if you’d like to make this into a long term
project. *Hint hint.

"""
from time import sleep ## sleep funciton to slow down the terminal

story = 'After fighting off a menacing zombie, you are left injured and stumble into an abandoned mansion. With only one leg remaining, you need to find a first aid kit fast or you may meet an untimely fate. You know there is a first aid kit somewhere in this mansion. You just need to find it. Good luck!' 

## initialising variables to be used later
swords = False
keys = False
firstAid = False
zombie = False
food = False
knife = False
crowbar = False
movesRemaining = 20

## a counter for the moves remaining
## every input decreases it 
def movesLeft(x):
    global movesRemaining
    movesRemaining -= x
    print(f"You now have {movesRemaining} minutes remaining.")
    if movesRemaining <= 0:
        print("Your injuries have gotten the better of you. Better luck next time!")
        quit()

## creating a function for each room makes navigation slightly easier
def hallWay():
    sleep(1) ## to avoid bursts of text
    directions = ['forward', 'left', 'right'] ## list of accepted directions
    movesLeft(1)
    print("You have made into the hallway. Behind you is the entrance you came from, but you don't want to go back out there! Would you like to go forward, left or right?")
    pathPicker = ""
    while pathPicker not in directions: ## cycle through until valid input is entered
        pathPicker = input("Choose forward, left or right: ").lower()
        if pathPicker == 'forward':
            livingRoom() ## calling the functions of other rooms
        elif pathPicker == 'left':
            bedroom()
        elif pathPicker == 'right':
            kitchen()
        else:
            print('Please choose from the available options. I know it might be tedious but please also spell it according to the prompt.')

def livingRoom():
    sleep(1)
    directions = ['backward', 'left', 'right']
    global swords ## calling variables to be changed/updated
    global keys
    movesLeft(1)
    if swords == False and keys == False: ## the process of collecting/interacting with an item
        print("You have entered the living room. Here you find a set of keys and some decorative swords. Would you like to pick them up?")
        haveSwordKeys = input('Yes or No: ').lower() ## to accept any accidental caps
        if haveSwordKeys == 'yes':
            swords = True ## updating the variable so it no longer triggers the if statement
            keys = True
            print("You now have a sword and a key in your inventory! Where would you like to go?")
    else: 
        print("You have entered the living room, which is now empty. It's actually quite depressing. Where would you like to go?")
    pathPicker = ""
    while pathPicker not in directions:
        pathPicker = input('Choose forward, left, right or backward: ').lower()
        if pathPicker == 'forward':
            print("You find a door towards a garden. You peek outside the window and it just looks so scary out there. Consider it a dead end.")
            movesLeft(1)
        elif pathPicker == 'left':
            bathroom()
        elif pathPicker == 'right':
            attic()
        elif pathPicker == 'backward':
            hallWay()
        else:
            print('Please choose from the available options. I know it might be tedious but please also spell it according to the prompt.')
        
def kitchen():
    sleep(1)
    directions = ['backward']
    global food
    global knife
    global movesRemaining
    movesLeft(1)
    if food == False and knife == False:
        print("You have entered the kitchen, where some food and a knife instantly catch your eye. Would you like to collect these items? ")
        haveFoodKnife = input('Yes or No: ').lower()
        if haveFoodKnife == 'yes': ## the food increases the amount of minutes remaining
            food = True
            knife = True
            print("You have now added these items to your inventory.")
            movesLeft(-3)
            print("There are no doors to your right or left. Ahead of you there is a pantry and the hallway is behind you Where would you like to go?")
    else:
        print("You have entered the kitchen. It's quite small and there are no doors to your right or left. Where would you like to go?")
    pathPicker = ""
    while pathPicker not in directions:
        pathPicker = input('Choose forward or backward: ').lower()
        if pathPicker == 'forward':
            print("You walk over to the pantry and the doors are jammed shut. Consider this a dead end.")
            movesLeft(1)
        elif pathPicker == 'backward':
            hallWay()
        else:
            print('Please choose from the available options. I know it might be tedious but please also spell it according to the prompt.')
        
def bedroom():
    sleep(1)
    directions = ['right', 'forward']
    global keys
    global zombie
    global swords
    global knife
    movesLeft(1)
    if keys == False:
        print("You have found the bedroom, but the door is locked. The key is somewhere in the house and you need to find it to enter. You turn around head back.")
        hallWay()
    else:
        if zombie == False:     
            print("You have found the bedroom. You use the key you found earlier to open the door.")
            zombieKiller()
        pathPicker = ""
        while pathPicker not in directions:
            pathPicker = input('Choose forward or right: ').lower()
            if pathPicker == 'forward':
                bathroom()
            elif pathPicker == 'right':
                hallWay()
            else:
                print('Please choose from the available options. I know it might be tedious but please also spell it according to the prompt.')

def bathroom():
    sleep(1)
    directions = ['right', 'backward']
    global crowbar
    movesLeft(1)
    bathroomStory = "You have now entered the bathroom. You see a bath tub, a toilet and a door back to the living room on your right."
    crowbarConfirm = "You have now added the crowbar to your inventory."
    crowbarCheck = "You also see a crowbar lying on the ground. Would you like to pick it up?"
    if crowbar == False:
        print(f"{bathroomStory} {crowbarCheck}")
        haveCrowbar = input("Yes or No: ").lower()
        if haveCrowbar == 'yes':
            crowbar = True
            print(crowbarConfirm)
    else:
        print(f"{bathroomStory}")
    pathPicker = ""
    while pathPicker not in directions:
        pathPicker = input('Choose right or backward: ').lower()
        if pathPicker == 'right':
            livingRoom()
        elif pathPicker == 'backward':
            bedroom()
        else:
            print('Please choose from the available options. I know it might be tedious but please also spell it according to the prompt.')

def attic():
    sleep(1)
    global crowbar
    global movesRemaining
    movesLeft(1)
    if crowbar == False:
        print("You have now reached the attic. However the door seems to be locked somehow, but not by a key. You might be able to pry it open with the right tools... Why not explore and see what you find?")
        livingRoom()
    else:
        print("You have now reached the attic. You use the crowbar to force the door open and you climb inside. You turn on the light... Oh wow! You have found the first aid kit! You're not a doctor but you give everything you have into fixing that leg of yours.")
        sleep(2)
        print(f"You've done it! You made it with {movesRemaining} minutes left! You are safe in the house and you're no longer at risk of dying. Well done on completing the game! You are a true adventurer!")
        quit()

def zombieKiller():
    sleep(1)
    global zombie
    global swords
    global knife
    fightStory1 = "It is a tough battle but you obliterate the and throw its dismantled corpse outside the window through a small crack you found!"
    fightStory2 = " With the zombie gone, you look around and see a door to a bathroom up ahead."
    print(f"You find a zombie! How did it even get in? That doesn't matter though. It needs to die. Are you ready to fight at the cost of 5 minutes?")
    killZombie = input("Yes or No: ").lower()
    if killZombie == 'yes':
        movesLeft(5)
        if swords == True and knife == True:
            print("Would you like to use your knife or sword for this battle?")
            choiceWeapon = input('Knife or Sword?: ').lower()
            print(f"You have chosen to fight. You enter the room and retrieve your {choiceWeapon} from your inventory. {fightStory1} The fight has drained you but you are rejuvenated by the food in your inventory! {fightStory2}")
        elif swords == True and knife == False:
            print(f"You have chosen to fight. You enter the room and retrieve your sword from your inventory. {fightStory1} The fight has drained you! You must find the first aid kit fast! {fightStory2}")
    else: 
        print("Well then you can't proceed any further in this room. You turn around and head back.")
        hallWay()
    zombie = True
    bedroom()

print("Hello! Welcome to Text Adventure! Would you like to begin?")
begin = input("Enter yes to begin your adventure: ").lower()
if begin == 'yes':
    print("Let's go!")
    sleep(1)
    name = input("What is your name? ")
    print(f"Okay {name}, fasten your seatbelt, and let's get to it... ")
    sleep(1)
    print (story)
    print("You will have '20 minutes' to get through the game, with every move reducing your time by a minute. Some acts will reduce it faster and some items will increase it. Make your choices wisely!")
    realBegin = ""
    while realBegin != 'yes' and realBegin != 'no':
        realBegin = input("Are you ready? Enter yes or no: ").lower()
        if realBegin == 'yes':
            hallWay()
        elif realBegin == 'no':
            quit()
        else:
            print("Please enter Yes or No: ")