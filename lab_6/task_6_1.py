"""
     Game "Catch the ball"
"""

import pygame
import math
import sys
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

FPS = 2
DISP_X = 800
DISP_Y = 600

score = 0

x, y, r = -1, -1, -1
lst_balls = list()
lst_rec = list()
my_font = pygame.font.SysFont('Sans bolt', 30)


def check():
    answer = mb.askyesno(
        title="Вопрос",
        message="Перенести данные?")
    if answer:
        s = entry.get()
        entry.delete(0, END)
        label['text'] = s


def roll_fig(balls, way):
    """Movement and reflection of goals"""
    bl_lst = list()
    for ball in balls:
        bl_angle = ball[-1]
        bl_x = ball[1][0]
        bl_y = ball[1][1]
        bl_r = ball[2]
        if bl_x + bl_r > DISP_X - way:
            bl_x = DISP_X - bl_r
            bl_angle = randint(180, 360)
            way *= 2
        elif bl_x - bl_r < way:
            bl_x = bl_r
            bl_angle = randint(0, 180)
            way *= 2
        elif bl_y + bl_r > DISP_Y - way:
            bl_y = DISP_Y - bl_r
            bl_angle = randint(90, 270)
            way *= 2
        elif bl_y - bl_r < way:
            bl_y = bl_r
            bl_angle = randint(-90, 90)
            way *= 2

        bl_x += way * math.cos(bl_angle * math.pi / 180)
        bl_y += way * math.sin(bl_angle * math.pi / 180)
        bl_lst.append((ball[0], (bl_x, bl_y), bl_r, bl_angle))
    return bl_lst


def new_fig(lst):
    """Draw new ball"""
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(50, 100)
    angle = randint(0, 360)

    color = COLORS[randint(0, 5)]
    lst.append((color, (x, y), r, angle))
    return lst


def click(event_click, fig_lst, name_fig):
    global lst_balls
    global lst_rec
    hit = False
    lst_tmp = list()
    for ball in fig_lst:
        x_bal = ball[1][0]
        y_bal = ball[1][1]
        r_bal = ball[2]
        if (((event_click[0] - x_bal) ** 2 +
           (event_click[1] - y_bal) ** 2) ** 0.5 <= r_bal):
            hit = True
        else:
            lst_tmp.append(ball)
    if name_fig == 'ball':
        lst_balls = lst_tmp
    elif name_fig == 'square':
        lst_rec = lst_tmp
    return hit


def show_score(score_show, record_show):
    """Display score"""
    text_surface = my_font.render(str(score_show), False, (0, 0, 0))
    screen.blit(text_surface, (20, 10))
    text_record = my_font.render('Record : ' + str(record_show),
                                 False, (0, 0, 0))
    screen.blit(text_record, (300, 10))


def display_update(score_sh, record_sh, balls, squares):
    screen.fill((230, 230, 230))
    show_score(score_sh, record_sh)
    for i in balls:
        circle(screen, *i[:-1])

    for square in squares:
        side = square[2]
        ring_r = side / 2
        rect(screen, square[0],
             (square[1][0] - ring_r, square[1][1] - ring_r, side, side))

    pygame.display.update()


def read_file():
    """
    Read or create file for saving record
    """
    try:
        fin = open('record.txt', 'r')
    except FileNotFoundError:
        fin = open('record.txt', 'w')
        print(0, a0, file=fin)
        fin.close()
        fin = open('record.txt', 'r')
    records = []
    for line_read in fin:
        records.append(int(line_read.strip()[-1]))
    fin.close()
    return max(records)


def save_record(record_num):
    """
    Save record in file "record.txt"
    :param record_num: :
    """
    name = input("Input your name \n")
    with open('record.txt', 'a') as f_out:
        print(name, record_num, file=f_out)


# Create a window
screen = pygame.display.set_mode((DISP_X, DISP_Y))
screen.fill((230, 230, 230))
pygame.display.set_caption('Catch the ball')

record_read = read_file()
record = record_read

display_update(score, record, lst_balls, lst_rec)

# Create object clock for creating delay
clock = pygame.time.Clock()
# Create main loop
finished = False
time = 0

speed = 50

new_fig(lst_balls)
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if click(event.pos, lst_balls, 'ball'):
                score += 1
                display_update(score, record, lst_balls, lst_rec)
            if click(event.pos, lst_rec, 'square'):
                score += 2
                display_update(score, record, lst_balls, lst_rec)
            if score > record:
                record = score
    lst_balls = roll_fig(lst_balls, speed)
    lst_rec = roll_fig(lst_rec, speed)
    if time == 5:
        lst_rec = new_fig(lst_rec)
    elif time >= 10:
        lst_balls = new_fig(lst_balls)
        time = 0
    time += 1
    display_update(score, record, lst_balls, lst_rec)
else:
    if record > record_read:
        save_record(record)

pygame.quit()
