##########################################################################
# Author: Samuca
#
# brief: Calculate the price of a trip
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

km = float(input("write down how many km you will travel: "))

#if you are under 200km, pay R$0,50 for each km
#if you are above 200km, pay R$0,45 for each km

if km < 200:
    print("Pay R${}".format(km*0.5))
else:
    print("Pay R${}".format(km*0.45))
