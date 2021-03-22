##########################################################################
# Author: Samuca
#
# brief: calculate a discount
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

value = float(input("Enter with your value: R$"))

discount = 5
new_value = (1-(discount/100)) * value
#other way
#new_value = value - (value*discount/100)

print("Your value with {}% discount is: R${:.2f}".format(discount, new_value))
