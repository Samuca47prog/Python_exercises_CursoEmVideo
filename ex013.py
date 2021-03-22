##########################################################################
# Author: Samuca
#
# brief: calculate a increase of salary
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

value = float(input("Enter with your salary: R$"))

add = 15
new_value = (1+(add/100)) * value
#other way
#new_value = value + (value*discount/100)

print(f"Congratulations!! You've gotten a salary increase of {add}%!!!")
print("Your salary now is: R${:.2f}".format(new_value))
