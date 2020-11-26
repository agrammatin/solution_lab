from random import randrange as rnd, choice
import tkinter as tk
import math
import time

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

root = tk.Tk()
fr = tk.Frame(root)
root.geometry(str(WINDOW_WIDTH) + 'x' + str(WINDOW_HEIGHT))
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class Ball:
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        self.x += self.vx
        self.y -= self.vy

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        pass
        # FIXME
        # return False


class Gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)
    ## FIXME: don't know how to set it...
    '''
    self.f2_power = 10
    self.f2_on = 0
    self.an = 1
    # self.id = canv.create_line(20,450,50,420,width=7) 
    # FIXME: don't know how to set it...
    '''

    def fire2_start(self, event):
        self.f2_on = 1


    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self, fill='orange')
        else:
            canv.itemconfig(self, fill='black')
        canv.coords(self, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self, fill='orange')
        else:
            canv.itemconfig(self, fill='black')


class Target:
    points = 0
    live = 1
    '''
    self.points = 0
    self.live = 1
    '''
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.id = canv.create_oval(0,0,0,0)
    ## self.id_points = canv.create_text(30,30,text = self.points,font = '28')
    ## self.new_target()

    def __init__(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(100, WINDOW_WIDTH - 100)
        y = self.y = rnd(100, WINDOW_HEIGHT - 100)
        r = self.r = rnd(20, 50)
        color = self.color = 'red'
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        # canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)
        # canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)


target_1 = Target()
screen1 = canv.create_text(400, 300, text='', font='28')
gun_1 = Gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun_1, target_1, screen1, balls, bullet
    # t1.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', gun_1.fire2_start)
    canv.bind('<ButtonRelease-1>', gun_1.fire2_end)
    canv.bind('<Motion>', gun_1.targetting)

    ## z = 0.03

    target_1.live = 1
    while target_1.live or balls:
        for b in balls:
            b.move()
            if b.hittest(target_1) and target_1.live:
                target_1.live = 0
                target_1.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за '
                                              + str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
        gun_1.targetting()
        gun_1.power_up()
    canv.itemconfig(screen1, text='')
    # canv.delete(gun)
    root.after(750, new_game)


new_game()

mainloop()
