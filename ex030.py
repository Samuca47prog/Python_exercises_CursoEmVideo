##########################################################################
# Author: Samuca
#
# brief: the classic: even or odd?
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

number = int(input("Write down your number: "))

if (number%2) == 0:
    print(f"number {number} is \033[1;36mEVEN\033[m")
else:
    print(f"number {number} is \033[1;36mODD\033[m")
