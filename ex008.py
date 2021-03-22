##########################################################################
# Author: Samuca
#
# brief: unit meter converter
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

m = float(input('Number in meters: '))

print(' in km: {:.3f} \n\
      \r in hm: {:.3f} \n\
      \r in dam: {:.3f} \n\
      \r in dm: {:.3f} \n\
      \r in cm: {:.3f} \n\
      \r in mmm: {:.3f} \n\
'.format((m/1000), (m/100), (m/10), (m*10), (m*100), (m*1000)))
    