#Branches and functions exercise
#A small choose your own adventure game
from sys import exit

input_prompt = "> "

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input(input_prompt)
    if isnumeric(choice):
        how_much = int(choice)
    else:
        dead("Please, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear?")
    print("* take honey")
    print("* taunt bear")
    print("* open door")
    print("* (other?)")
    bear_moved = False

    while True:
        choice = input(input_prompt)

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("It stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    print("* flee for your life")
    print("* eat your head")
    print("* (other?)")
    choice = input(input_prompt)

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    print("* right")
    print("* left")
    print("* (other?)")

    choice = input(input_prompt)

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
