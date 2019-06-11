import pygame

class Ball(pygame.sprite.Sprite):
    color = 0, 0, 0
    def __init__(self, pos, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, 50])
        self.image.fill(Ball.color)
        pygame.draw.circle(self.image, (255, 255, 255), (25, 25), 25)
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos[0] - 0.5 * self.rect.width, pos[1] - self.rect.height)
        self.speed = speed

    def move(self, ball_x_direction, ball_y_direction):
        self.rect.move_ip(0, ball_y_direction * self.speed)
        if ball_x_direction == 0:
            return
        elif ball_x_direction > 0:
            self.rect.move_ip(self.speed, 0)
        else:
            self.rect.move_ip(-self.speed, 0)

    def get_rect(self):
        return self.rect