##########################################################################
# Author: Samuca
#
# brief: read a city and says if it starts with "santo"
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

#split() returns all parts of the string in a list, separated by " "
#we can separate it by any other char, giving it in the ("<char>")
city = str(input("Write down your city: ")).split()

#it doesn't matter how you write 'santo', it will be always capital letter
#because of upper(), and it will be compared with "SANTO"
print(city[0].upper() == "SANTO")
#once it is a logical test, it will return True or False!
