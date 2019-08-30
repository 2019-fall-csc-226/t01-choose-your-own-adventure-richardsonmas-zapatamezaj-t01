######################################################################
# Author: Mason Richardson Jose Zapata Meza  TODO: Change this to your names
# Username: Richardsonmas zapatamezaj     TODO: Change this to your usernames
#
# Assignment: T01: Choose Your Own Adventure
#
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem
######################################################################
from time import sleep

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False         # You start out not dead, which is good.

# Asks the user to input their name.
username = input("What do they call you, unworthy adversary? ")

#########################################################################################################
# The following is the first part of the story. Don't change this section.
print()
print("Welcome,", username, ", to the labyrinth.")
sleep(delay)
print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
sleep(delay * 2)
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print()
sleep(delay)

#########################################################################################################
# This is an example chapter. Your story will follow a similar structure.
# You will learn more by NOT copy and pasting this section. Write your section on your own, and when you get stuck,
# refer to this code to help you get unstuck. Of course, raise your hand if you get really stuck.

direction = input("Which direction would you like to go? [North/South/East/West]" )

if direction == "North":
    # Good choice!
    print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
    sleep(delay)
elif direction == "South":
    # Oh... Bad choice
    print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
    sleep(delay)
    print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
    print("Running seems like a good idea now. But... it's really, really dark.")
    print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
    print("He eats you. You are delicious.")
    dead = True
else:
    # Neutral choice
    print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
    sleep(delay)

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
# TODO Add your part of the story here. Keep in mind you may NOT be coming right after the example above.
print("You come upon three doors.")
sleep(delay * 2)
print("The one of the left has a light glowing from underneath.")
sleep(delay * 4)
print("The one in the middle looks old and cracked.")
sleep(delay * 4)
print("The one on the right is made of rusted metal.")

direction = input("Which door will you choose? [Left, Middle, Right]")
if direction.lower() == "right":
    # good choice
    print("You can barely see because the room is so dark and dusty. \nYou light your torch and see the room is filled to the brim with gold and jewels!.")
    sleep(delay * 4)
    print("Congratulations, you're rich!")
    choice = 0

elif direction.lower() == "left":
    # worst choice
    print("You step through the door onto a thin sheet of ice. Below the ice, electricity arcs from one electric eel to another.\nYou turn quickly to walk back out the door and...")
    sleep(delay * 3)
    print("A golden dragon appears, he offers to help if and only if you can guess a number between 1 to 10")
    number = int(input("What number do you choose?"))
    if number >= 6:
        print("He offers you a ride to safety, you come out with no major injuries.")
        choice = 2
    else:
        print("The ice breaks! You are electrocuted while you are drowned... ")
        dead = True
        choice =1
else:
    # boring choice
    print("You open the middle door. Behind the door you find a long passage with stairs that seem to go up forever.")
    sleep(delay * 2)
    print("...")
    sleep(delay * 2)
    print("....")
    sleep(delay * 2)
    print(".....")
    sleep(delay * 2)
    print("You realize this tunnel is leading to nowhere and close your eyes, wishing for an escape.")
    sleep(delay)
    choice = 2


# TODO Don't forget to check if your user is dead at the end of your chapter!
if choice == 0:
    print("You collect your treasure and you move on to the next part of the cave")
elif choice == 1:
    print("You die, try again to test your fate again!")
else:
    print("You open your eyes and you are in a new place. You are alive, but somewhat bored and disappointed.")


#########################################################################################################

# The following is the end of the story. Don't change this section, unless you really want to
# (though it may not be used in the final story. Or will it...)
#print("Look at that! You made it to the end of the story without dying! ")
#print("Congratulations... now go play again and find an interesting way to perish. ")
#print("Try again by hitting the green play button.")
