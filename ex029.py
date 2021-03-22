##########################################################################
# Author: Samuca
#
# brief: Electronic radar
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

speed = float(input("Write down your speed: "))

#the road speed limit is 80 km/h
speed_lim = 80

if speed > speed_lim:
    #you were over the speed limit!
    #you have to pay R$7,00 for each km above the limit
    km_over = speed - speed_lim
    print("\033[1;31m!!You were over the speed limit!!\033[m")
    print("Pay \033[1;33mR${:.2f}\033[m for your {}km/h over"\
          .format(km_over*7, km_over))
        
else:
    print("keep calm and go on")
