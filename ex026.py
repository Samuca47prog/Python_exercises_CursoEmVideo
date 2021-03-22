##########################################################################
# Author: Samuca
#
# brief: Returns a report about a letter in a sentece
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

sentence = str(input("Write down your sentence: ")).upper().strip()

#str.count("char")
print("There are {} in the sentence".format(sentence.count("A")))
#str.find("char") -> returns the first appearence
print("Firts Appearence: position {}".format(sentence.find("A")+1))
#str.rfind("char") -> returns the last appearence (from the right)
print("Last Appearence: position {}".format(sentence.rfind("A")+1))
