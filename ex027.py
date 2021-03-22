##########################################################################
# Author: Samuca
#
# brief: Returns the first and the last name in a string
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

name = str(input("Write down your name: ")).split()

print("Your first name is {}".format(name[0]))
print("Your last name is {}".format(name[-1]))
