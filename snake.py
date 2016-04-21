__author__ = 'Тупиков Павел'
__version__ = 1.0

import turtle
import time
import random


class Figure(object):
    def __init__(self, x, y, h=10, w=10):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        my_ttl = turtle.Turtle()
        my_ttl.hideturtle()
        self.my_ttl = my_ttl


class Cross(Figure):
    def __init__(self, x, y, h=10, w=10):
        super(Cross, self).__init__(x, y)

    def draw(self, color):
        self.my_ttl.color(color)
        self.my_ttl.penup()
        self.my_ttl.setpos(self.x, self.y)
        self.my_ttl.pendown()
        self.my_ttl.goto(self.x + self.w, self.y + self.h)
        self.my_ttl.penup()
        self.my_ttl.setpos(self.x, self.y + self.h)
        self.my_ttl.pendown()
        self.my_ttl.goto(self.x + self.w, self.y)


class Square(Figure):
    def __init__(self, x, y, h=10, w=10):
        super(Square,self).__init__(x, y)

    def draw(self, color):
        self.my_ttl.color(color)
        self.my_ttl.penup()
        self.my_ttl.setpos(self.x, self.y)
        self.my_ttl.pendown()
        self.my_ttl.begin_fill()
        self.my_ttl.goto(self.x + self.h, self.y)
        self.my_ttl.goto(self.x + self.h, self.y + self.h)
        self.my_ttl.goto(self.x, self.y + self.h)
        self.my_ttl.goto(self.x, self.y)
        self.my_ttl.end_fill()


class VerticalLine(Cross):
    def __init__(self, y_down, y_up, x):
        self.y_down = y_down
        self.y_up = y_up
        self.x = x
        self.v = list()
        while self.y_down <= self.y_up:
            c = Cross(self.x, self.y_down)
            self.v.append(c)
            self.y_down += c.h

    def line_draw(self):
        for c in self.v:
            c.draw('red')


class GorLine(Cross):
    def __init__(self, x_left, x_right, y):
        self.x_left = x_left
        self.x_right = x_right
        self.y = y
        self.g = list()
        while self.x_left <= self.x_right:
            c = Cross(self.x_left, self.y)
            self.g.append(c)
            self.x_left += c.w

    def line_draw(self):
        for c in self.g:
            c.draw('red')


class MainSn(Square):
    def __init__(self, x_sn, y_sn, l, direction):
        self.y_sn = y_sn
        self.x_sn = x_sn
        self.l = l
        self.direction = direction
        self.sn = list()
        self.sx = list()
        self.sy = list()
        i = 0
        while i < self.l:
            s = Square(self.x_sn, self.y_sn)
            self.sn.append(s)
            if self.direction == 'up':
                self.y_sn -= s.h
                i += 1
                print(self.y_sn - s.h)
            if self.direction == 'down':
                self.y_sn -= s.h
                i += 1
            if self.direction == 'left':
                self.x_sn += s.w
                i += 1
            if self.direction == 'right':
                self.x_sn += s.w
                i += 1
            self.sx.append(self.x_sn)
            self.sy.append(self.y_sn)
        self.h = s.h
        self.w = s.w
        self.sx.clear()
        self.sy.clear()
        self.x_head = self.x_sn
        self.y_head = self.y_sn

    def sn_draw(self):
        for c in self.sn:
            c.draw('green')

    def move(self):
        sq = self.sn[0]
        self.sn.pop(0)
        sq.draw('#ffffff')
        if self.direction == 'up':
            self.y_head += self.h
        if self.direction == 'down':
            self.y_head -= self.h
        if self.direction == 'left':
            self.x_head -= self.w
        if self.direction == 'right':
            self.x_head += self.w
        s = Square(self.x_head, self.y_head)
        self.sn.append(s)


class Apple(Figure):
    def __init__(self, x_ap, y_ap, h=10, w=10):
        super(Apple,self).__init__(x_ap, y_ap)
        self.x_ap = x_ap
        self.y_ap = y_ap

    def ap_draw(self):
        self.x_ap = random.randint(-44, 44)*10
        self.y_ap = random.randint(-29, 29)*10
        self.my_ttl.color('orange')
        self.my_ttl.penup()
        self.my_ttl.setpos(self.x_ap, self.y_ap)
        self.my_ttl.pendown()
        self.my_ttl.begin_fill()
        self.my_ttl.goto(self.x_ap + self.h, self.y_ap)
        self.my_ttl.goto(self.x_ap + self.h, self.y_ap + self.h)
        self.my_ttl.goto(self.x_ap, self.y_ap + self.h)
        self.my_ttl.goto(self.x_ap, self.y_ap)
        self.my_ttl.end_fill()


sn = MainSn(0, 0, 3, 'up')
apple = Apple(10,10)


def turn_left():
    if sn.direction != 'right':
        sn.direction = 'left'


def turn_right():
    if sn.direction != 'left':
        sn.direction = 'right'


def turn_up():
    if sn.direction != 'down':
        sn.direction = 'up'


def turn_down():
    if sn.direction != 'up':
        sn.direction = 'down'


def eating():
    if (sn.x_head == apple.x_ap)&(sn.y_head == apple.y_ap):
        s = Square(sn.x_head, sn.y_head)
        sn.sn.append(s)
        apple.ap_draw()


def end():
    if (sn.x_head <= -450) or (sn.x_head >= 450) or (sn.y_head <= -300) or (sn.y_head >= 300):
        game=False
    else:
        game=True
    return game


def main():


    game = 1
    turtle.tracer(0, 0)
    turtle.hideturtle()
    ver = VerticalLine(-300, 300, 450)
    ver1 = VerticalLine(-300, 300, -450)
    gor = GorLine(-450, 450, -300)
    gor1 = GorLine(-450, 450, 300)
    ver.line_draw()
    ver1.line_draw()
    gor.line_draw()
    gor1.line_draw()
    sn.sn_draw()
    turtle.onkeypress(turn_left,"Left")
    turtle.onkeypress(turn_right,"Right")
    turtle.onkeypress(turn_up,"Up")
    turtle.onkeypress(turn_down,"Down")
    turtle.listen()
    apple.ap_draw()
    while game:
        sn.move()
        game = end()
        eating()
        sn.sn_draw()
        time.sleep(0.1)
        turtle.update()
    turtle.home()
    turtle.write("Вы проиграли!!!", font=("Arial", 20, "bold"), align="right")
    time.sleep(2)

if __name__ == '__main__':
    main()