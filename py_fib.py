#!/usr/bin/env python3

import pygame
from pygame_tools import *

class Fib(GameScreen):
    def __init__(self):
        pygame.init()
        size = Point(1400, 750)
        super().__init__(pygame.display.set_mode(size), size)
        self.center = Point(self.window_size.x / 2, self.window_size.y / 2)
        self.colors = {
                'bg': 'black',
                'fg': 'white',
                }
        self.starting_size = 1
        self.max_size = max(self.window_size.x, self.window_size.y) * 2

    def draw(self):
        count = 0
        prev2_size = 0
        prev_size = 0
        size = self.starting_size
        rect = pygame.Rect(*self.center, 0, 0)
        density = 50
        while size < self.max_size:
            if (c := count % 4) == 0:
                new_pos = Point(
                        rect.x,
                        rect.y - size
                        )
                curve = get_bezier_curve_points(
                        Point(new_pos.x, new_pos.y + size),
                        Point(new_pos.x, new_pos.y),
                        Point(new_pos.x + size, new_pos.y),
                        density
                        )
            elif c == 1:
                new_pos = Point(
                        rect.x + prev_size,
                        rect.y
                        )
                curve = get_bezier_curve_points(
                        Point(new_pos.x, new_pos.y),
                        Point(new_pos.x + size, new_pos.y),
                        Point(new_pos.x + size, new_pos.y + size),
                        density
                        )
            elif c == 2:
                new_pos = Point(
                        rect.x - prev2_size,
                        rect.y + prev_size
                        )
                curve = get_bezier_curve_points(
                        Point(new_pos.x + size, new_pos.y),
                        Point(new_pos.x + size, new_pos.y + size),
                        Point(new_pos.x, new_pos.y + size),
                        density
                        )
            elif c == 3:
                new_pos = Point(
                        rect.x - size,
                        rect.y - prev2_size
                        )
                curve = get_bezier_curve_points(
                        Point(new_pos.x + size, new_pos.y + size),
                        Point(new_pos.x, new_pos.y + size),
                        Point(new_pos.x, new_pos.y),
                        density
                        )
            rect = pygame.Rect(*new_pos, size, size)
            pygame.draw.rect(self.screen, self.colors['fg'], rect, 1) # draw the boxes
            pygame.draw.lines(self.screen, self.colors['fg'], False, curve) # draw the curve
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
