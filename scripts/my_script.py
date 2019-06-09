"""Script to run some part of my project."""

# Imports
import os, sys
# This adds the directory above to our Python path
# so that we can add import our custom python module code into this script
sys.path.append('../')

import pygame
from pygame.locals import *

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')

from my_module.main_screen_funcs import load_image

# Constants we will use for screen
size = 1200, 750
black = 0, 0, 0

# Set up the main screen
screen = pygame.display.set_mode(size)

# Loop of animation and all the program this game needs
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    
    screen.fill(black)
    pygame.display.flip()