##########################################################################
# Author: Samuca
#
# brief: sin, cos, and tan of an angle 
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

from math import sin, cos, tan, radians

a = float(input("Write down an angle: "))

#converts the angle in degrees to radians, to use it in the functions
a = radians(a)

print("sin={:.3f} \ncos={:.3f} \ntan={:.3f}".format(sin(a), cos(a), tan(a)))
