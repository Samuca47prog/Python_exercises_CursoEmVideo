##########################################################################
# Author: Samuca
#
# brief: currency converter
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

#considering $1 = R$5,72 and E1 = R$6,80, in 03/08/2021

real = float(input('Value in real: R$'))

print("With R${:.2f} you can buy ${:.2f}".format(real, (real/5.72)))
print("you can also buy {:.2f}".format(real/6.8))
