##########################################################################
# Author: Samuca
#
# brief: is this a leap year?
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

from datetime import date

year = int(input("Write down any year (0 for the actual year): "))

if year == 0:
    #returns the actual year
    year = date.today().year

#to be a leap year, we have 3 conditions:
    #be diviseble by 4
    #not to be multiple of 100
    #except 400 multiples
    
if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
    print(f"year {year} is a leap year")
else:
    print(f"year {year} is NOT a leap year")
