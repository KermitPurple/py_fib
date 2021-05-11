import pygame
from pygame_tools import *

class Fib(GameScreen):
    def __init__(self):
        pygame.init()
        real_size = Point(600, 600)
        size = Point(real_size.x // 4, real_size.y // 4)
        super().__init__(pygame.display.set_mode(real_size), real_size, size)
        self.center = Point(size.x / 2, size.y / 2)

    def draw(self):
        ...

    def update(self):
        self.screen.fill('black')
        self.draw()

def main():
    Fib().run()

if __name__ == '__main__':
    main()
