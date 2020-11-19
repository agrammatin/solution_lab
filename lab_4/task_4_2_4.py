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

pygame.display.set_caption('Smile')
# Yellow circle
circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (0, 0, 0), (200, 175), 100, 1)

# Left eye
circle(screen, (255, 0, 0), (150, 150), 20)
circle(screen, (0, 0, 0), (150, 150), 20, 1)
circle(screen, (0, 0, 0), (150, 150), 8)

# Left eyebrow
polygon(screen, (0, 0, 0), [(180, 145), (100, 100),
                                (105, 93), (185, 137)])

# Right eye
circle(screen, (255, 0, 0), (250, 150), 15)
circle(screen, (0, 0, 0), (250, 150), 15, 1)
circle(screen, (0, 0, 0), (250, 150), 8)

# Right eyebrow
polygon(screen, (0, 0, 0), [(220, 145), (300, 115),
                                (295, 108), (215, 137)])

# Mouth
rect(screen, (0, 0, 0), (150, 220, 100, 20))


'''
rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
polygon(screen, (255, 255, 0), [(100, 100), (200, 50),
                                (300, 100), (100, 100)])
polygon(screen, (0, 0, 255), [(100, 100), (200, 50),
                              (300, 100), (100, 100)], 5)
circle(screen, (0, 255, 0), (200, 175), 50)
circle(screen, (255, 255, 255), (200, 175), 50, 5)
'''

# Update window
pygame.display.update()

# Create object clock for creating delay
clock = pygame.time.Clock()
FPS = 50
# Create main loop
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
