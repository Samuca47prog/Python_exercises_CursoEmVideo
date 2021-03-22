##########################################################################
# Author: Samuca
#
# brief: change and gives information about a string
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

#strip() means that the spaces before and after the string won't be considered
name = str(input("Write down your name: ")).strip()

print("analysing your name...")

print("It in Upper: {}".format(name.upper()))
print("It in Lower: {}".format(name.lower()))

#//// LEN()
#//// STR.COUNT()
#len(name) gives the number of char in the str (including ' ')
#name.count(' ') will return the number of ' ' in the str
#name.count('x') can count any char in the str
print("Number of letters: {}".format(len(name) - name.count(' ')))

#name.find('x') returns the index of the first appearence of that char
#print("Your first name has {} letters".format(name.find(' ')))

#//// SPLIT()
#other way is with split(), that will create a list separating the 
#chars by the space, if any other char be said (this char is not included).
sep = name.split()
print(sep)
print("Yout first name is {}, it has {} letters".format(sep[0], len(sep[0])))
