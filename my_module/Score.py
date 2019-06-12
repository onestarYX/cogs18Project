""" The file which defines Score class """

import pygame

class Score(pygame.sprite.Sprite):
    color = 255, 255, 255
    score = 0

    def __init__(self):
        """
        Constructor for Score objects.

        =====
        Parameters:
            None
        
        =====
        Returns:
            A Score object
        """

        pygame.sprite.Sprite.__init__(self)

        # Initialize the font object
        self.font = pygame.font.Font(None, 22)
        msg = 'Score: {}'.format(self.score)

        # Basically the image here is just the msg string
        self.image = self.font.render(msg, 1, self.color)
        # Use a rectangle to wrap up the string
        self.rect = self.image.get_rect()

    def update(self):
        """
        The funtion which  tells us what Score would update in every frame

        =====
        Parameters:
            None

        =====
        Returns:
            None
        """

        # We just need to update the msg using the latest score.
        msg = 'Score: {}'.format(self.score)
        self.image = self.font.render(msg, 1, self.color)