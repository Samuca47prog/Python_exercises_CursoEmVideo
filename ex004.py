##########################################################################
# Author: Samuca
#
# brief: gives many infos about a str
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

something = input('anything: ')

#once 'something' is a object str, we ca apply it many methods such as:

print('Type? ', type(something))
print('Is there only spaces? ', something.isspace())
print('Is it a number? ', something.isnumeric())
print('Is it a letter? ', something.isalpha())
print('Is it a alphanumeric? ', something.isalnum())
print('Is it upper? ', something.isupper())
print('Is it lower? ', something.islower())
print('Is it captalized?', something.istitle())
