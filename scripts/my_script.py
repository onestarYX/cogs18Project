"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import os, sys
sys.path.append('../')

import pygame
from pygame.locals import *

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')

# Imports
from my_module.functions import my_func, my_other_func

# Constants we will use for screen
size = 1200, 750
black = 0, 0, 0

screen = pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    
    screen.fill(black)
    pygame.display.flip()