"""
     Game "Catch the ball"
"""

import pygame
from pygame.draw import *
from random import randint

# It is library initialization after import
pygame.init()

B_GROUND = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

FPS = 1

x, y, r = -1, -1, -1
lst_balls = list()
my_font = pygame.font.SysFont('Sans bolt', 130)


def new_ball():
    """Draw new ball"""
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(50, 100)

    color = COLORS[randint(0, 5)]
    lst_balls.append((color, (x, y), r))
    # circle(screen, color, (x, y), r)


def click(event_click, balls):
    global lst_balls
    hit = False
    lst_tmp = list()
    for ball in balls:
        x_bal = ball[1][0]
        y_bal = ball[1][1]
        r_bal = ball[2]
        if (((event_click[0] - x_bal) ** 2 +
           (event_click[1] - y_bal) ** 2) ** 0.5 <= r_bal):
            hit = True
        else:
            lst_tmp.append(ball)
    lst_balls = lst_tmp
    return hit


def show_score(score_show):
    text_surface = my_font.render(str(score_show), False, (0, 0, 0))
    screen.blit(text_surface, (20, 10))


def display_update(score_sh, balls):
    screen.fill((230, 230, 230))
    show_score(score_sh)
    for i in balls:
        circle(screen, *i)

    pygame.display.update()


# Create a window
screen = pygame.display.set_mode((800, 600))
screen.fill((230, 230, 230))
pygame.display.set_caption('Catch the ball')


score = 0
display_update(score, lst_balls)

# Create object clock for creating delay
clock = pygame.time.Clock()
# Create main loop
finished = False
time = 0
new_ball()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if click(event.pos, lst_balls):
                score += 1
                display_update(score, lst_balls)
    if time >= 10:
        new_ball()
        time = 0
    time += 1
    print(time)
    display_update(score, lst_balls)

pygame.quit()
