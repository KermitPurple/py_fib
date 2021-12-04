import pygame
from pygame_tools import *

def bezier_curve(p0: Point, p1: Point, p2: Point, density: int) -> [Point, ...]:
    """
    B(t) = (1-t)^2 * p0 + 2(1-t)t * p1 + t^2 * p2
    0 <= t <= 1
    https://en.wikipedia.org/wiki/B%C3%A9zier_curve
    """
    result = []
    for i in range(density):
        t = i / density
        result.append(Point(
            (1 - t) ** 2 * p0.x + 2 * (1 - t) * t * p1.x + t ** 2 * p2.x,
            (1 - t) ** 2 * p0.y + 2 * (1 - t) * t * p1.y + t ** 2 * p2.y
            ))
    return result

class Fib(GameScreen):
    def __init__(self):
        pygame.init()
        real_size = Point(600, 600)
        size = real_size
        super().__init__(pygame.display.set_mode(real_size), real_size, size)
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
        density = 30
        while size < self.max_size:
            if (c := count % 4) == 0:
                new_pos = Point(
                        rect.x,
                        rect.y - size
                        )
                curve = bezier_curve(
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
                curve = bezier_curve(
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
                curve = bezier_curve(
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
                curve = bezier_curve(
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
