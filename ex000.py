##############################################################################
# Author: Samuca
# 
# brief: create the 100+  files of the list
#
# this is a list exercise available on youtube:
#    https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##############################################################################

import os

for d in range(1, 116):
    if d in range(1, 10):
        diretorio = 'ex00'
        
    if d in range(10, 100):
        diretorio = 'ex0'
        
    if d in range(100, 116):
        diretorio = 'ex'
        
    #create the files
    if not os.path.exists(diretorio + str(d)):
        f = open(diretorio + str(d) + '.py', 'w+')
        print(diretorio + str(d))
        
        #write the header
        f.write("\
##########################################################################\n\
# Author: Samuca\n\
#\n\
# brief: \n\
#\n\
# this is a list exercise available on youtube:\n\
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-\n\
##########################################################################\n\
    ")
