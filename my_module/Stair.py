from my_module.main_screen_funcs import load_image

class Stair():
    def __init__(self, image, speed = 10):
        self.image = load_image(image)
        self.speed = speed
        self.pos = self.image.get_rect().move(0, 700)

    def renderImage(self):
        return self.image

    def getPos(self):
        return self.pos

    def move(self):
        self.pos = self.pos.move(0, -self.speed)