""" The file which defines the Ball class """
import pygame

class Ball(pygame.sprite.Sprite):
    color = 0, 0, 0
    def __init__(self, pos, screen, x_speed, y_speed):
        """
        The constructor for Ball objects

        =====
        Parameters:
            pos--tuple:
                the tuple containing two integers which are the initial coordinates
                for the ball's mid bottom point (which is the point where in real
                life a ball gets touched with the ground)
            screen--Surface:
                the Surface object which is the main screen of the game
            x_speed--Int:
                the initial speed of ball's horizontal motion
            y_speed--Int:
                the initial speed of ball's vertical motion
        =====
        Returns:
            A Ball object
        """
        pygame.sprite.Sprite.__init__(self)

        # The image of the ball is basically drawing a ball in a square
        self.image = pygame.Surface([20, 20])
        self.image.fill(Ball.color)
        pygame.draw.circle(self.image, (255, 255, 255), (10, 10), 10)
        self.rect = self.image.get_rect()
        # Calculate the ball's top left point's coordinate based on its
        # mid bottom point's coordinate.
        self.rect.move_ip(pos[0] - 0.5 * self.rect.width, pos[1] - self.rect.height)
        self.area = screen.get_rect()
        self.x_speed = x_speed
        self.y_speed = y_speed


    def move(self, ball_x_direction, ball_y_direction):
        """
        The function which responds to ball's motion based on player's input

        =====
        Parameters:
            ball_x_direction--Int:
                Could be 1, 0, -1, which respectively represents moving right,
                staying, moving left
            ball_y_direction--Int:
                Could be 1 or -1, which respectively represents moving downward
                and moving upward
        =====
        Returns:
            None
        """
        # Move the ball vertically
        self.rect.move_ip(0, ball_y_direction * self.y_speed)

        # Move the ball horizontally
        if ball_x_direction == 0:
            return
        elif ball_x_direction > 0:
            self.rect.move_ip(self.x_speed, 0)
        else:
            self.rect.move_ip(-self.x_speed, 0)


    def is_out_of_bound(self):
        """
        The function which checks whether or not the ball goes out of the
        screen.

        =====
        Parameters:
            None
        
        =====
        Returns:
            A boolean value which indicates whether or not the ball goes
            out of the screen.
        """
        if self.rect.bottom < self.area.top or self.rect.top > self.area.bottom:
            return True
        else:
            return False


    def set_speed_lv1(self):
        """
        The function which increases ball's speed to level 1.

        =====
        Parameters:
            None
        
        =====
        Returns:
            None
        """
        self.x_speed = 8
        self.y_speed = 4


    def set_speed_lv2(self):
        """
        The function which increases ball's speed to level 2.

        =====
        Parameters:
            None
        
        =====
        Returns:
            None
        """
        self.x_speed = 10
        self.y_speed = 6


    def get_rect(self):
        """
        The function which returns the ball's rect.

        =====
        Parameters:
            None
        
        =====
        Returns:
            Rect object of the ball
        """
        return self.rect