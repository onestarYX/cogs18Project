import pygame

class Stair(pygame.sprite.Sprite):
    images = []
    current_stairs = 0
    def __init__(self, pos, screen, speed = 10):
        pygame.sprite.Sprite.__init__(self)
        self.image = Stair.images[0]
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