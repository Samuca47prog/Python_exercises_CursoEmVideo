##########################################################################
# Author: Samuca
#
# brief: pick a name randomly
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################


import random
from math import floor

names = []

for i in range(1, 5):
    name = input(f"name {i}: ")
    names.append(name)

index = floor((random.random()) * len(names))
print("\nthe name picked was {}".format(names[index]))

#other way
#random.choice() picks one element randomly in the list given
picked = random.choice(names)
print("\nThe name picked was: {}".format(picked))
