##########################################################################
# Author: Samuca
#
# brief: ask for a number, give it it times 2 and 3 and its squareroot
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

number = int(input('Number: '))

#this is a power syntax, but it also calculates roots
#square_root = number ** (1/2)

#other way is using pow(base, pot)
square_root = pow(number, (1/2))

print(f'Its double: {number*2} and its triple: {number*3}')
print('Its square root: {:.2f}'.format(square_root))
