##########################################################################
# Author: Samuca
#
# brief: calculate a car rent
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

#data: 
#day rent = R$60,00
#Km traveled = R$0,15

days = int(input("How many days have you been with the car? "))
km = float(input("How many km have you traveled? "))


pay = (days * 60) + (km * 0.15)

print("you have to pay: R${:.2f}".format(pay))
