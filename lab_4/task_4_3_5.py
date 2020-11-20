"""
     Task 4_2_4 Draw mountains
"""

import pygame
import sys
import math
from pygame.draw import *

# It is library initialization after import
pygame.init()

# Create a window
screen = pygame.display.set_mode((1200, 800))

# Define the colors we will use in RGB format
BLACK = (0,   0,   0,)
WHITE = (255, 255, 255)
CLR_BACK_1 = (255, 228, 196)
CLR_BACK_2 = (255, 192, 203)
CLR_BACK_3 = (240, 240, 200)
CLR_BACK_4 = (190, 150, 180)
CLR_SUN = (255, 255, 0)
CLR_MOUNT_BROWN = (210, 105, 30)
CLR_MOUNT_BROWN_Dark = (170, 50, 50)
CLR_MOUNT_PURPLE = (50, 30, 50)
CLR_BIRD = (47, 79, 79)


# Draw background
rect(screen, CLR_BACK_1, (0, 0, 1200, 170))
rect(screen, CLR_BACK_2, (0, 170, 1200, 170))
# rect(screen, (169, 169, 169), (0, 170, 1200, 170), 1)
rect(screen, CLR_BACK_3, (0, 340, 1200, 170))
# rect(screen, (169, 169, 169), (0, 340, 1200, 170), 1)
rect(screen, CLR_BACK_4, (0, 510, 1200, 290))

# Draw san
circle(screen, CLR_SUN, (570, 170), 70)

# Mountains brown
polygon(screen, CLR_MOUNT_BROWN, [
    (5, 370), (15, 320),
    *((15 + i, 320 - i**2/340) for i in range(235)),
    (290, 170), (310, 200),
    (480, 290), (550, 280),
    (590, 310), (5, 370)
])
polygon(screen, CLR_MOUNT_BROWN, [
    (590, 310), (650, 250),
    (700, 260), (720, 230),
    *((720 + i, 230 - i ** 2 / 220) for i in range(150)),
    *((868 + i + 12, 125 + i ** 2 / 28) for i in range(-25, 25)),
    (950, 190), (1000, 180),
    (1070, 220),
    (1110, 200), (1200, 250),
    (590, 310)
])
# Mountains dark_brown


# Mountains purple
polygon(screen, CLR_MOUNT_PURPLE, [
    (0, 800), (0, 400), (150, 430),
    *((150 + i + 350 + 12, 780 - i ** 2 / 380) for i in range(-350, 50)),
    (750, 680),
    # (1200, 500),
    *((750 + i + 112, 730 - i ** 2 / 300) for i in range(-50, 200)),
    # (1200, 800),
    *((1100 + i + 120, 500 + i ** 2 / 250) for i in range(-100, -10)),
    (1200, 800),
    (0, 800)
])

# Draw bird
polygon(screen, CLR_BIRD, [
    (500, 80),
    *((500 + i, 80 + i ** 2 / 60) for i in range(0, 20)),
    (535, 90),
    (570, 80),
    (530, 100),
    (500, 80)
])
'''
polygon(screen, CLR_BIRD, [
    (500, 80),
    *((500 + i, 80 + 5 * math.cos(2*math.pi*i/50 + math.pi/2))
      for i in range(30)),
    (535, 90),
    (570, 80),
    (530, 100),
    (500, 80)
])
'''
# Update window
pygame.display.update()

# Create object clock for creating delay
clock = pygame.time.Clock()
FPS = 100
# Create main loop
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
