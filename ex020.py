##########################################################################
# Author: Samuca
#
# brief: shuffles the names of a list
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

from random import shuffle

names = []

for i in range(1, 5):
    name = input(f"name {i}: ")
    names.append(name)

shuffle(names)

print(f"order of names = {names}")
