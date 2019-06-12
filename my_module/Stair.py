""" The file which defines the Stair class"""

import pygame

class Stair(pygame.sprite.Sprite):
    # The number of current stairs existed in the game
    current_stairs = 0
    color = 255, 255, 255

    def __init__(self, pos, screen, speed = 10):
        """
        Constructor for Stair objects

        =====
        Parameters:
            pos--tuple:
                The tuple which contains two integers to tell Stair's initial
                coordinates.
            screen--Surface:
                The main screen of the program which is used to pass the size
            speed--Int:
                The initial speed of stairs going up.
        """
        pygame.sprite.Sprite.__init__(self)

        # Define an area of rectangle and fill it with color to represent
        # our stairs.
        self.image = pygame.Surface([80, 8])
        self.image.fill(Stair.color)
        # Wrap up the stair image with rectangle and move it to its initial
        # position
        self.rect = self.image.get_rect().move(pos[0], pos[1])
        self.area = screen.get_rect()
        self.speed = speed

    def update(self):
        """
        This function tells us how Stair objects would update for every frame

        =====
        Parameters:
            None
        
        =====
        Returns:
            None
        """

        # In every the stairs just move up by their speed. 
        self.rect = self.rect.move(0, -self.speed)

        # Check whether or not the stair has left the screen. If
        # it does, destruct itself and remove it from every sprite
        # groups.
        if self.rect.bottom < self.area.top:
            self.kill()
            Stair.current_stairs -= 1


    def set_speed_lv1(self):
        """
        The function which increases stair speed to level 1.

        =====
        Parameters:
            None
        
        =====
        Returns:
            None
        """
        self.speed = 4


    def set_speed_lv2(self):
        """
        The function which increases stair speed to level 2.

        =====
        Parameters:
            None
        
        =====
        Returns:
            None
        """
        self.speed = 6


    def get_pos(self):
        """
        This function returns the position of the stair.

        =====
        Parameters:
            None
        
        =====
        Returns:
            A tuple which contains the coordinates of the stair's rectangle's
            top left point.
        """
        return (self.rect.left, self.rect.top)

    def get_rect(self):
        """
        The function which returns a stair's rectangle.

        =====
        Parameters:
            None
        
        =====
        Returns:
            A rect object which wraps up some stair
        """
        return self.rect