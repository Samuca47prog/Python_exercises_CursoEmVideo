##########################################################################
# Author: Samuca
#
# brief: plays a mp3 song
#
# this is a list exercise available on youtube:
#   https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
##########################################################################

#pygame modulo has a lot of tools to work with games, such as:
# load images
# play songs

import pygame

#initializate the module
pygame.init()

#load the song
pygame.mixer.music.load("ex021.mp3")

#play the song
pygame.mixer.music.play()

#wait the song ends 
pygame.event.wait()
