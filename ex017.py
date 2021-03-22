##########################################################################
# Author: Samuca
#
# brief: calculate pythagoras 
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

collegiate1 = float(input("Enter with the first collegiate: "))
collegiate2 = float(input("Enter with the second collegiate: "))

hypotenuse = collegiate1 ** 2 + collegiate2 ** 2
hypotenuse = hypotenuse ** (1/2)

print("The hypotenuse is {:.2f}".format(hypotenuse))

#other way
from math import hypot

co = float(input("Co: "))
ca = float(input("Ca: "))

hi = hypot(ca, co)

print(f"Hypotenuse ia: {hi}")
