"""
File description: Script to run Don't Fall.
Author: Yixing Wang
PID: A14521981
Last edit Time: 06/11
"""

""" Import some python offcial modules """
import sys
# This adds the directory above to our Python path
# so that we can add import our custom python module code into this script
sys.path.append('../')

""" Import pygame package and all its local pre-defined macros. """
import pygame
pygame.init()
from pygame.locals import *

""" Import my own modules and functions """
from my_module.Stair import Stair
from my_module.Ball import Ball
from my_module.Score import Score
from my_module.main_screen_funcs import load_image, rand_x_offset, rand_y_offset, correct_x_pos



""" Constants for the screen """
size = 500, 400
black = 0, 0, 0
max_stairs = 10


""" Set up main screen and background. """
# Set up the main screen
screen = pygame.display.set_mode(size)
# Configure the background
background = pygame.Surface(size)
background = background.convert()
# Give the background a color
background.fill(black)


""" Give some initial values for the game """
# Initial speed of stairs going up when we start the game.
start_y_speed = 2
# Initial speed of ball moving horizontally
start_x_speed = 4
# Initial postion of the first stair
initial_pos = 216, size[1] - 20

# Set a clock to keep track of the FPS
clock = pygame.time.Clock()


""" All sprite groups we will need for this game. """
# Group of all objects in this game.
all_objects = pygame.sprite.RenderUpdates()
# Group of stairs
stairs = pygame.sprite.Group()
# Keep track of the lowest stair (or last created stair) using GroupSingle
# container, so next time we can create the new stair at some distance 
# below the lowest stair.
lowest_stair = pygame.sprite.GroupSingle()


""" Initialize the first stair and add it to all the groups """
new_stair = Stair(initial_pos, screen, start_y_speed)
all_objects.add(new_stair)
stairs.add(new_stair)
lowest_stair.add(new_stair)
# Increase the stairs count.
Stair.current_stairs = 1


""" Initialize the ball """
first_stair_pos = new_stair.get_pos()
first_stair_rect = new_stair.get_rect()
# Set ball's initial position to be the middle of the first stair.
ball_init_pos = (first_stair_pos[0] + 0.5 * first_stair_rect.width, first_stair_pos[1])
ball = Ball(ball_init_pos, screen, start_x_speed, start_y_speed)
# Add the ball into the all_objects group.
all_objects.add(ball)

""" Initialize the score msg """
score = Score()
all_objects.add(score)


# Loop of animation when this game is running
while True:

    """ Listen for player's manually exit operation """
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    """ Check whether or not we need to create new stairs. """
    if Stair.current_stairs < max_stairs:
        # Get the current lowest stair postion.
        last_pos = lowest_stair.sprite.get_pos()
        # Calculate for the postion of the new stair by adding randomized distance
        # to last_pos.
        new_pos = [last_pos[0] + rand_x_offset(), last_pos[1] + rand_y_offset()]
        # To avoid the stair shows up out of the screen.
        correct_x_pos(new_pos)
        # Create a stair
        new_stair = Stair(new_pos, screen, start_y_speed)
        all_objects.add(new_stair)
        stairs.add(new_stair)
        lowest_stair.add(new_stair)
        Stair.current_stairs += 1

    # Erase objects from current the screen by painting the screen with
    # background.
    all_objects.clear(screen, background)

    """ Listen for the key press """
    key = pygame.key.get_pressed()
    ball_x_direction = key[K_RIGHT] - key[K_LEFT]
    # Set the direction of ball's motion as 1 because by gravity we
    # always want the ball to fall down.
    ball_y_direction = 1

    # Keep track for the point at the ball which decides whether or not
    # the ball can be held by the stairs.
    balance_point = ball.get_rect().midbottom

    """ A loop to check whether the ball should be held by any stair """
    for stair in stairs.sprites():
        stair_rect = stair.get_rect()
        # If the ball's positon is right "on" the stair, the ball should go
        # up with the stair.
        if balance_point[1] == stair_rect.top and \
        balance_point[0] >= stair_rect.left and \
        balance_point[0] <= stair_rect.right:
            ball_y_direction = -1
            break
        else:
            ball_y_direction = 1

    # Increase the score
    Score.score += 1


    """ Increase the difficulty of the game when the score is between
        600 and 1000, or 2000 and 2400 """
    # Since when we increase the difficulty, the ball might be falling down,
    # so the distance between the ball and newly created stair might be
    # messed up (b.c. the distance between the two has to be a multiple
    # of the sum of ball's and the stairs' speed), so we want to increase the
    # difficulty when the ball is held by a stair.
    if ball_y_direction == -1:
        if Score.score in range(600, 1000):
            # Set the start_y_speed for future use in creating stair with the
            # correct speed.
            start_y_speed = 4
            for stair in stairs.sprites():
                stair.set_speed_lv1()
            ball.set_speed_lv1()
        elif Score.score in range(2000, 2400):
            start_y_speed = 6
            for stair in stairs.sprites():
                stair.set_speed_lv2()
            ball.set_speed_lv2()

    # Update all objects' postions by calling update to every sprite object
    # in the group.
    all_objects.update()
    # Move the ball according to its postion and player's input.
    ball.move(ball_x_direction, ball_y_direction)

    # Draw objects with updated postions and return the list of rectangular
    # pixels changed. We only want to update the changed area for the purpose
    # of improving FPS.
    dirty = all_objects.draw(screen)
    pygame.display.update(dirty)

    # Check if we lose
    if ball.is_out_of_bound():
        break
        sys.exit()

    # Calculate the FPS and print it for debuging purpose.
    # Comment it out if no need to use.
    clock.tick()
    # print(clock.get_fps())

print('Your score: ', Score.score)