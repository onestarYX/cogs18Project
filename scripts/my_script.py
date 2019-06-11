"""Script to run some part of my project."""

# Imports
import sys
# This adds the directory above to our Python path
# so that we can add import our custom python module code into this script
sys.path.append('../')

import pygame
from pygame.locals import *

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')


from my_module.Stair import Stair
from my_module.Ball import Ball
from my_module.main_screen_funcs import rand_x_offset, rand_y_offset, correct_x_pos

# Constants we will use for screen
size = 1200, 750
black = 0, 0, 0
max_stairs = 10


# Set up the main screen
screen = pygame.display.set_mode(size)
background = pygame.Surface(size)
background.fill(black)

start_speed = 5
initial_pos = 300, 750

all_objects = pygame.sprite.RenderUpdates()
stairs = pygame.sprite.Group()
lowest_stair = pygame.sprite.GroupSingle()

new_stair = Stair('stair.png', initial_pos, screen, start_speed)
all_objects.add(new_stair)
stairs.add(new_stair)
lowest_stair.add(new_stair)
Stair.current_stairs = 1

first_stair_pos = new_stair.get_pos()
first_stair_rect = new_stair.get_rect()
ball_init_pos = (first_stair_pos[0] + 0.5 * first_stair_rect.width, first_stair_pos[1])
ball = Ball(ball_init_pos, start_speed)

all_objects.add(ball)


# Loop of animation and all the program this game needs
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    if Stair.current_stairs < max_stairs:
        last_pos = lowest_stair.sprite.get_pos()
        new_pos = [last_pos[0] + rand_x_offset(), last_pos[1] + rand_y_offset()]
        correct_x_pos(new_pos)
        # print('x change: {} and y change: {}'.format(new_pos[0] - last_pos[0], new_pos[1] - last_pos[1]))
        new_stair = Stair('stair.png', new_pos, screen, start_speed)
        all_objects.add(new_stair)
        stairs.add(new_stair)
        lowest_stair.add(new_stair)
        Stair.current_stairs += 1

    all_objects.clear(screen, background)


    key = pygame.key.get_pressed()
    ball_x_direction = key[K_RIGHT] - key[K_LEFT]
    balance_point = ball.get_rect().midbottom
    ball_y_direction = 1

    for stair in stairs.sprites():
        stair_rect = stair.get_rect()
        if balance_point[1] == stair_rect.top and \
        balance_point[0] >= stair_rect.left and \
        balance_point[0] <= stair_rect.right:
            print("on the plate!")
            ball_y_direction = -1
            break
        else:
            ball_y_direction = 1

    if(ball_y_direction == 1):
        print('Not on the plate ......')

    all_objects.update()
    ball.move(ball_x_direction, ball_y_direction)

    dirty = all_objects.draw(screen)
    pygame.display.update(dirty)