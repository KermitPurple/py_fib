import pygame
from pygame_tools import *

class Fib(GameScreen):
    def __init__(self):
        pygame.init()
        real_size = Point(600, 600)
        size = Point(real_size.x // 4, real_size.y // 4)
        super().__init__(pygame.display.set_mode(real_size), real_size, size)
        self.center = Point(self.window_size.x / 2, self.window_size.y / 2)
        self.colors = {
                'bg': 'black',
                'fg': 'white',
                }
        self.starting_size = 1

    def draw(self):
        count = 0
        prev2_size = 0
        prev_size = 0
        size = self.starting_size
        rect = pygame.Rect(*self.center, 0, 0)
        while size < 300:
            if (c := count % 4) == 0:
                new_pos = Point(
                        rect.x,
                        rect.y - size
                        )
            elif c == 1:
                new_pos = Point(
                        rect.x + prev_size,
                        rect.y
                        )
            elif c == 2:
                new_pos = Point(
                        rect.x - prev2_size,
                        rect.y + prev_size
                        )
            elif c == 3:
                new_pos = Point(
                        rect.x - size,
                        rect.y - prev2_size
                        )
            rect = pygame.Rect(*new_pos, size, size)
            pygame.draw.rect(self.screen, self.colors['fg'], rect, 1)
            prev2_size = prev_size
            prev_size, size = size, prev_size + size
            count += 1

    def update(self):
        self.screen.fill(self.colors['bg'])
        self.draw()

def main():
    Fib().run()

if __name__ == '__main__':
    main()
