##########################################################################
# Author: Samuca
#
# brief: returns the bigger and smaller between 3 numbers
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

#inicializating, the first number is the bigger and the smaller
num = int(input("Write down the number 1: "))
bigger = num
smaller = num

for i in range(2, 4):
    num = int(input(f"Write down the number {i}: "))
    
    if num > bigger:
        bigger = num
    
    if num < smaller:
        smaller = num

print(f"the bigger: {bigger}")
print(f"the smaller: {smaller}")
