##########################################################################
# Author: Samuca
#
# brief: Game! Guess what the number is
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
#########################################################################

from random import random
from math import floor
from time import sleep

#random return an number between 0 and 1
raffle = floor(random()*5)+1
#it is possible to generate a random int number with randint(a,b) from random

number  = int(input("Guess a number between 1 and 5: "))

print("Proceeding...")
#wait for 3 seconds
sleep(3)

if number == raffle:
    print("Congratulations!!")
else:
    print(f"my number was {raffle}, dumb")
