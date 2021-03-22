##########################################################################
# Author: Samuca
#
# brief: multiplication table
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

number = int(input('Number: '))

print('-' * 12)

for i in range (1, 11):
    print('{} x {:2.0f} = {}'.format(number, i, (number*i)))
    
print('-' * 12)
    