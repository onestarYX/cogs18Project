import pygame

class Ball(pygame.sprite.Sprite):
    color = 0, 0, 0
    def __init__(self, pos, screen, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill(Ball.color)
        pygame.draw.circle(self.image, (255, 255, 255), (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos[0] - 0.5 * self.rect.width, pos[1] - self.rect.height)

        self.area = screen.get_rect()

        self.speed = speed

    def move(self, ball_x_direction, ball_y_direction):
        self.rect.move_ip(0, ball_y_direction * self.speed)
        if ball_x_direction == 0:
            return
        elif ball_x_direction > 0:
            self.rect.move_ip(self.speed, 0)
        else:
            self.rect.move_ip(-self.speed, 0)

    def is_out_of_bound(self):
        if self.rect.bottom < self.area.top or self.rect.top > self.area.bottom:
            return True
        else:
            return False

    def get_rect(self):
        return self.rect