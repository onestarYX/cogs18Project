"""Script to run some part of my project."""

# Imports
import sys, random
# This adds the directory above to our Python path
# so that we can add import our custom python module code into this script
sys.path.append('../')

import pygame
from pygame.locals import *

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')

# from my_module.main_screen_funcs import load_image
from my_module.Stair import Stair

# Constants we will use for screen
size = 1200, 750
black = 0, 0, 0
max_stairs = 10


# Set up the main screen
screen = pygame.display.set_mode(size)

start_speed = 10
pos0 = 100, 750

stairs = pygame.sprite.Group()
lowest_stair = pygame.sprite.GroupSingle()

new_stair = Stair('stair.png', pos0, screen, start_speed)
stairs.add(new_stair)
lowest_stair.add(new_stair)
Stair.current_stairs = 1

# Loop of animation and all the program this game needs
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    if Stair.current_stairs < max_stairs:
        last_pos = lowest_stair.sprite.getPos()
        new_pos = (last_pos[0] + 30, last_pos[1] + 200)
        new_stair = Stair('stair.png', new_pos, screen, start_speed)
        stairs.add(new_stair)
        lowest_stair.add(new_stair)
        Stair.current_stairs += 1
        print(Stair.current_stairs)

    stairs.update()
    

    screen.fill(black)
    stairs.draw(screen)
    pygame.display.flip()