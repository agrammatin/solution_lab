"""
     Example draw circle after mouse click
"""

import pygame
from pygame.draw import *

# It is library initialization after import
pygame.init()

# Create a window
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Click mouse and draw ring')

RED = (255, 0, 0)
BLUE = (0, 0, 255)


def draw_window(lst_point):
    """
    Clear screen and draw rings from lst_point
    :param lst_point: list params for draw circle
    """
    screen.fill((0, 0, 0))
    for i in lst_point:
        circle(screen, *i)
    pygame.display.update()


lst_ring = list()

# Update window
pygame.display.update()

# Create object clock for creating delay
clock = pygame.time.Clock()
FPS = 100
# Create main loop
finished = False
time_del = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                lst_ring.append((RED, event.pos, 50, 2))
            elif event.button == 3:
                lst_ring.append((BLUE, event.pos, 50, 6))
            draw_window(lst_ring)
    time_del += 1
    if time_del > 200:
        lst_ring = lst_ring[1:]
        draw_window(lst_ring)
        print(lst_ring)
        time_del = 0

pygame.quit()
