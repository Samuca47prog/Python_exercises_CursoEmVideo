##########################################################################
# Author: Samuca
#
# brief: returns if a str has "silva" 
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

#strip() takes out the spaces before and after the str
name = str(input("write down your full name: ")).strip()

print("Is there Silva in the name? {}".format("SILVA" in name.upper()))

#in is a Python operator!
