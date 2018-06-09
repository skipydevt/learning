# trialing some of the looping and branching function

import os
os.system('cls')

name = input("what is your name? ")

if name  == "Keith":
    print("Hello again")
elif name == "Lindsay":
    print("Has Keith been banned from the pc?")
else:
    print("Where's Keith?")




input("\n\nPress enter to try new things")

print("three year old simulator")

import random

whichq = random.randint(1,3)

if whichq == 1:
    print("Why is the sun yellow?\n")
elif whichq == 2:
    print("Why are elephants grey?\n")
elif whichq == 3:
    print("Why are my eyes blue?\n")

response = input()

while response != "because":
    response = input("Why?\n")

print("Oh... OK.")

input("Press enter")
