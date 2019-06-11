"""A collection of function for doing my project."""

import os, sys, random
sys.path.append('../')

import pygame
from pygame.locals import *

def my_func():
    pass

def my_other_func():
    pass

def load_image(name):
    """
    Load the image for the screen.

    This function is modified based on the function found in
    https://www.pygame.org/docs/tut/ChimpLineByLine.html

    ======
    Parameters:
        name--String:
            The name of the image file we use.
        colorKey:
            The color key we will use as a filter to the image.
    ======
    Returns:
        None
    """

    fullname = os.path.join('../assets/', name)

    try:
        image = pygame.image.load(fullname)
    except:
        print ('Cannot load image: ' + name)
        raise (SystemExit)

    image = image.convert()

    return image

def rand_x_offset():
    return random.choice((1, -1)) * random.randrange(50, 350)

def rand_y_offset():
    return random.randrange(100, 280)

def correct_x_pos(pos):
    if pos[0] > 900:
        print('true')
        pos[0] -= (pos[0] - 900)
    elif pos[0] < 0:
        print('true')
        pos[0] = 100