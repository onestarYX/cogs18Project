import pygame
from my_module.main_screen_funcs import load_image

class Stair(pygame.sprite.Sprite):
    current_stairs = 0
    def __init__(self, image, pos, screen, speed = 10):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image)
        self.rect = self.image.get_rect().move(pos[0], pos[1])
        self.area = screen.get_rect()
        self.speed = speed

    def update(self):
        self.rect = self.rect.move(0, -self.speed)
        if self.rect.bottom < self.area.top:
            self.kill()
            Stair.current_stairs -= 1

    def get_pos(self):
        return (self.rect.left, self.rect.top)

    def get_rect(self):
        return self.rect