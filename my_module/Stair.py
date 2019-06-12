import pygame

class Stair(pygame.sprite.Sprite):
    current_stairs = 0
    color = 255, 255, 255
    def __init__(self, pos, screen, speed = 10):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([80, 8])
        self.image.fill(Stair.color)
        self.rect = self.image.get_rect().move(pos[0], pos[1])
        self.area = screen.get_rect()
        self.speed = speed

    def update(self):
        self.rect = self.rect.move(0, -self.speed)
        if self.rect.bottom < self.area.top:
            self.kill()
            Stair.current_stairs -= 1

    def set_speed_lv1(self):
        self.speed = 4

    def set_speed_lv2(self):
        self.speed = 6

    def get_pos(self):
        return (self.rect.left, self.rect.top)

    def get_rect(self):
        return self.rect