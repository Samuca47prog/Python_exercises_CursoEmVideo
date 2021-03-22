##########################################################################
# Author: Samuca
#
# brief: areas and painting calculator
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

#considerations: 1L of ink can paint 2m²

#^
height = float(input('Height: '))
#>
width = float(input('Width: '))

area = height * width
#liters are the half of m²
liters = area/2

print('For this wall of {}x{}, or {:.3f}m2, you will need {:.2f}L of ink'\
      .format(height, width, area, liters))
