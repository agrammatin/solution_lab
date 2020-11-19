"""
     Task 4_2_4 Python is amazing
"""

import pygame
import sys
import math
from pygame.draw import *


def draw_regular_polygon(
        surface, color, vertex_count, radius, position, thick=0, angle=0.0):
    if angle != 0:
        angle = math.pi/angle
    n, r = vertex_count, radius
    x, y = position
    pygame.draw.polygon(surface, color, [
        (x + r * math.cos(2 * math.pi * j / n + angle),
         y + r * math.sin(2 * math.pi * j / n + angle))
        for j in range(n)
    ], thick
    )


# It is library initialization after import
pygame.init()

# Create a window
screen = pygame.display.set_mode((1000, 800))
screen.fill((30, 30, 30))
pygame.display.set_caption('Python is amazing')

# Draw body
circle(screen, (255, 128, 64), (500, 850), 270)

# Draw head
circle(screen, (255, 192, 203), (500, 420), 250)
# Draw nose
polygon(screen, (139, 69, 19), [(480, 420), (520, 420), (500, 450)])
polygon(screen, (0, 0, 0), [(480, 420), (520, 420), (500, 450)], 1)
# Draw lip
polygon(screen, (255, 0, 0), [(370, 480), (620, 480), (500, 570)])
polygon(screen, (0, 0, 0), [(370, 480), (620, 480), (500, 570)], 1)
# Draw eyes
circle(screen, (100, 149, 237), (420, 350), 50)
circle(screen, (0, 0, 0), (420, 350), 50, 1)
circle(screen, (100, 149, 237), (580, 350), 50)
circle(screen, (0, 0, 0), (580, 350), 50, 1)
# Draw pupils
ellipse(screen, (0, 0, 0), (405, 350, 25, 20))
ellipse(screen, (0, 0, 0), (570, 350, 25, 20))
# Draw heir
color_pink = (255, 0, 255)
num = -4
x_start = 500
y_start = 160
for i in range(9):
    draw_regular_polygon(screen, color_pink, 3, 40,
                         (x_start + num * 40,
                          y_start + abs(num) * 15),
                         angle=6-(num * 0.5))
    draw_regular_polygon(screen, (0, 0, 0), 3, 40,
                         (x_start + num * 40,
                          y_start + abs(num) * 15), 1,
                         angle=6-(num * 0.5))
    num += 1

# Draw hands
polygon(screen, (255, 192, 203), [(50, 20), (90, 20),
                                  (290, 645), (250, 655)])
ellipse(screen, (255, 192, 203), (50, 0, 100, 150))
ellipse(screen, (255, 255, 255), (50, 0, 100, 150), 1)
polygon(screen, (255, 192, 203), [(910, 20), (950, 20),
                                  (750, 655), (710, 645)])
ellipse(screen, (255, 192, 203), (850, 0, 100, 150))
ellipse(screen, (255, 255, 255), (850, 0, 100, 150), 1)

# Draw shoulders
color_orange = (255, 128, 64)
draw_regular_polygon(screen, color_orange, 5, 75, (270, 650))
draw_regular_polygon(screen, (0, 0, 0), 5, 75, (270, 650), 1)

draw_regular_polygon(screen, color_orange, 5, 75, (730, 650), angle=6)
draw_regular_polygon(screen, (0, 0, 0), 5, 75, (730, 650), 1, angle=6)

# Draw text
rect(screen, (0, 255, 0), (0, 0, 1000, 100))
rect(screen, (0, 0, 0), (0, 0, 1000, 100), 1)
pygame.font.init()
my_font = pygame.font.SysFont('Sans bolt', 130)
text_surface = my_font.render('PYTHON is AMAZING', False, (0, 0, 0))
screen.blit(text_surface, (20, 10))

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
