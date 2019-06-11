import pygame
from my_module.main_screen_funcs import load_image

class Stair(pygame.sprite.Sprite):
    def __init__(self, image, speed = 10):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image)
        self.speed = speed
        self.rect = self.image.get_rect().move(0, 750)

    def renderImage(self):
        return self.image

    def getPos(self):
        return self.rect

    def update(self):
        self.rect = self.rect.move(0, -self.speed)