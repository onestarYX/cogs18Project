"""A collection of function for doing my project."""

import os, sys, random
sys.path.append('../')

import pygame
from pygame.locals import *


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
    """
    The function which return a random integer to be used for increase of
    distance in x direction for stairs.

    =====
    Parameters:
        None
    
    =====
    Returns:
        A integer which is the distance
    """
    return random.choice((1, -1)) * random.randrange(0, 144, 24)


def rand_y_offset():
    """
    The function which return a random integer to be used for increase of
    distance in y direction for stairs.

    =====
    Parameters:
        None
    
    =====
    Returns:
        A integer which is the distance
    """
    return random.randrange(48, 144, 24)


def correct_x_pos(pos):
    """
    The function which corrects stair's x coordinate in order to
    avoid the stair's position being somewhere out of the screen.

    =====
    Parameters:
        pos--list:
            the ball's coordinate list.
    =====
    Returns:
        None
    """
    if pos[0] > 420:
        pos[0] = 408 - random.randrange(0, 72, 24)
    elif pos[0] < 0:
        pos[0] = random.randrange(0, 72, 24)