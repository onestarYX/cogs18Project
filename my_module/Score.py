import pygame

class Score(pygame.sprite.Sprite):
    color = 255, 255, 255
    score = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 22)
        msg = 'Score: {}'.format(self.score)
        self.image = self.font.render(msg, 1, self.color)
        self.rect = self.image.get_rect()

    def update(self):
        msg = 'Score: {}'.format(self.score)
        self.image = self.font.render(msg, 1, self.color)