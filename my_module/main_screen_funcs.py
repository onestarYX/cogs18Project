"""A collection of function for doing my project."""

import os, sys
sys.path.append('../')

import pygame
from pygame.locals import *

def my_func():
    pass

def my_other_func():
    pass

def load_image(name, colorkey=None):
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

    fullname = os.path.join('assets', name)

    try:
        image = pygame.image.load(fullname)
    except (pygame.error, message):
        print ('Cannot load image:' + name)
        raise (SystemExit, message)

    image = image.convert()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
        
    return image, image.get_rect()