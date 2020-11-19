"""
    Example 1, 2
"""

import pygame
import sys
from pygame.draw import *


# It is library initialization after import
pygame.init()

# Create a window
screen = pygame.display.set_mode((400, 400))
screen.fill((230, 230, 230))

pygame.display.set_caption('Домик')
# Draw rectangle (color), (position)
rect(screen, (255, 0, 255), (100, 100, 200, 200))
N = 10
h = (300 - 100) // (N + 1)
x = 100 + h
for i in range(N):
    color_line = (255, 255, 255)
    line(screen, color_line, (x, 100), (x, 300))
    x += h

rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
polygon(screen, (255, 255, 0), [(100, 100), (200, 50),
                                (300, 100), (100, 100)])
polygon(screen, (0, 0, 255), [(100, 100), (200, 50),
                              (300, 100), (100, 100)], 5)
circle(screen, (0, 255, 0), (200, 175), 50)
circle(screen, (255, 255, 255), (200, 175), 50, 5)

# Update window
pygame.display.update()

# Create object clock for creating delay
clock = pygame.time.Clock()
FPS = 30
# Create main loop
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
