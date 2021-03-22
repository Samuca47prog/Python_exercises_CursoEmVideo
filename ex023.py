##########################################################################
# Author: Samuca
#
# brief: returns the unit, ten, hundred and thausands part of a number
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

number = int(input("write down a four digits number: "))

#turning the number into a str, it will be easier to prints its digits
    #n = str(number)
    #print("unit: {}".format(n[3]))
    #print("ten: {}".format(n[2]))
    #print("hundred: {}".format(n[1]))
    #print("thausands: {}".format(n[0]))
#this way above returns an error if we send a less then 4 digits number!

# {number // x} returns the int part of the division by x

#taking its UNIT
n = number // 1 % 10
print(f"Unit: {n}")

#taking its TEN
n = number // 10 % 10
print(f"Unit: {n}")

#taking its HUNDRED
n = number // 100 % 10
print(f"Unit: {n}")

#taking its THAUSAND
n = number // 1000 % 10
print(f"Unit: {n}")

#I was changed for GitHub
