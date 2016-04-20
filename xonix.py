#!/usr/bin/env python

import curses
import locale
import time
from random import randint, choice


class XonixBoard:
    def __init__(self, scr, char=ord('*')):
        self.state = {}
        self.scr = scr
        self.char = char
        self.scr.clear()
        Y, X = self.scr.getmaxyx()
        self.X, self.Y = X-2, Y-2-1
        self.balls = []
        self.old_balls = []
        self.game_cursor = []

        self.external_line_Y_min = 0
        self.external_line_Y_max = self.Y
        self.external_line_X_min = 0
        self.external_line_X_max = self.X

        self.internal_line_Y_min = 3
        self.internal_line_Y_max = self.Y-1
        self.internal_line_X_min = 3
        self.internal_line_X_max = self.X-2

        curses.noecho()
        curses.cbreak()
        self.scr.keypad(1)

        border_line = '+'+(self.X*'-')+'+'
        self.scr.addstr(0, 0, border_line)
        self.scr.addstr(self.external_line_Y_max+1, 0, border_line)
        for y in range(0, self.external_line_Y_max):
            self.scr.addstr(1+y, 0, '|')
            self.scr.addstr(1+y, self.external_line_X_max+1, '|')
        self.scr.refresh()

        border_line = '+'+((self.X-6)*'-')+'+'
#        self.scr.addstr(3, 3, border_line)
        self.scr.addstr(self.internal_line_Y_min,
                        self.internal_line_X_min, border_line)
#        self.scr.addstr(self.Y-1, 3, border_line)
        self.scr.addstr(self.internal_line_Y_max,
                        self.internal_line_X_min, border_line)
        for y in range(self.internal_line_Y_min, self.Y):
            self.scr.addstr(y, self.internal_line_X_min, '|')
#            self.scr.addstr(y, self.X-2, '|')
            self.scr.addstr(y, self.internal_line_X_max, '|')
        self.scr.refresh()

    def generate_balls(self, number_of_balls=5):
        for i in range(number_of_balls):
            self.balls.append((randint(4, self.Y-1), randint(4, self.X-7),
                               randint(0, 7)))  # N - 0, E - 2, S - 4, W - 6
        self.old_balls = self.balls[:]

    def game_run(self):
        curses.curs_set(0)
        for i in range(0, len(self.balls)):
            y, x = self.old_balls[i][:2]
            old_coord = "Y = {}, X = {}".format(y, x)
            self.scr.addstr(self.Y+1, 4, old_coord)
            y, x, z = self.balls[i]
            coord = "Y = {}, X = {}, Z = {}".format(y, x, z)
            self.scr.addstr(self.Y+2, 4, coord)
            self.scr.refresh()
            if y+1 > self.Y-2:
                if z == 3:
                    z = 1
                elif z == 4:
                    z = choice([1, 7])
                elif z == 5:
                    z = 7
            if y-1 < 4:
                if z == 0:
                    z = choice([3, 5])
                elif z == 1:
                    z = 3
                elif z == 7:
                    z = 5
            if x+1 > self.X-4:
                if z == 1:
                    z = 7
                elif z == 2:
                    z = choice([7, 5])
                elif z == 3:
                    z = 5
            if x-1 < 4:
                if z == 5:
                    z = 3
                elif z == 6:
                    z = choice([1, 3])
                elif z == 7:
                    z = 1

            if z == 0:
                old_y, old_x = self.old_balls[i][:2]
                self.old_balls[i] = (y, x, z)
                self.scr.move(old_y, old_x)
                self.scr.echochar(' ')
                self.scr.move(y, x)
                self.scr.echochar('*')
                self.balls[i] = (y-1, x, z)
            elif z == 1:
                old_y, old_x = self.old_balls[i][:2]
                self.old_balls[i] = (y, x, z)
                self.scr.move(old_y, old_x)
                self.scr.echochar(' ')
                self.scr.move(y, x)
                self.scr.echochar('*')
                self.balls[i] = (y-1, x+1, z)
            elif z == 2:
                old_y, old_x = self.old_balls[i][:2]
                self.old_balls[i] = (y, x, z)
                self.scr.move(old_y, old_x)
                self.scr.echochar(' ')
                self.scr.move(y, x)
                self.scr.echochar('*')
                self.balls[i] = (y, x+1, z)
            elif z == 3:
                old_y, old_x = self.old_balls[i][:2]
                self.old_balls[i] = (y, x, z)
                self.scr.move(old_y, old_x)
                self.scr.echochar(' ')
                self.scr.move(y, x)
                self.scr.echochar('*')
                self.balls[i] = (y+1, x+1, z)
            elif z == 4:
                old_y, old_x = self.old_balls[i][:2]
                self.old_balls[i] = (y, x, z)
                self.scr.move(old_y, old_x)
                self.scr.echochar(' ')
                self.scr.move(y, x)
                self.scr.echochar('*')
                self.balls[i] = (y+1, x, z)
            elif z == 5:
                old_y, old_x = self.old_balls[i][:2]
                self.old_balls[i] = (y, x, z)
                self.scr.move(old_y, old_x)
                self.scr.echochar(' ')
                self.scr.move(y, x)
                self.scr.echochar('*')
                self.balls[i] = (y+1, x-1, z)
            elif z == 6:
                old_y, old_x = self.old_balls[i][:2]
                self.old_balls[i] = (y, x, z)
                self.scr.move(old_y, old_x)
                self.scr.echochar(' ')
                self.scr.move(y, x)
                self.scr.echochar('*')
                self.balls[i] = (y, x-1, z)
            elif z == 7:
                old_y, old_x = self.old_balls[i][:2]
                self.old_balls[i] = (y, x, z)
                self.scr.move(old_y, old_x)
                self.scr.echochar(' ')
                self.scr.move(y, x)
                self.scr.echochar('*')
                self.balls[i] = (y-1, x-1, z)
    def get_key(self):
        self.scr.nodelay(1)
        c = self.scr.getch()
        if c != -1:
            if c == curses.KEY_UP:
                print "UP"
            elif c == curses.KEY_DOWN:
                print "DOWN"
            elif c == curses.KEY_LEFT:
                print "LEFT"
            elif c == curses.KEY_RIGHT:
                print "RIGHT"
            else:
                pass


#        curses.curs_set(0)
#        center_y, center_x = self.Y/2, self.X/2
#        self.scr.move(center_y, center_x)
#        self.scr.addch('*')
#        for y in range(center_y, self.Y-1):
#            time.sleep(0.1)
#            self.scr.move(y, center_x)
#            self.scr.echochar('*')
#            self.scr.move(y-1, center_x)
#            self.scr.echochar(' ')


def erase_menu(stdscr, menu_y):
    stdscr.move(menu_y, 0)
    stdscr.clrtoeol()
    stdscr.move(menu_y+1, 0)
    stdscr.clrtoeol()


def display_menu(stdscr, menu_y):
    erase_menu(stdscr, menu_y)
    stdscr.addstr(menu_y, 4, 'Some text')


def keyloop(stdscr):
    stdscr.clear()
    stdscr_y, stdscr_x = stdscr.getmaxyx()
    menu_y = (stdscr_y-3)-1
    display_menu(stdscr, menu_y)
    stdscr.refresh()

    subwin = stdscr.subwin(stdscr_y-4, stdscr_x, 0, 0)
    board = XonixBoard(subwin, char=ord('*'))
    board.generate_balls()
    while True:
        time.sleep(0.09)
        board.game_run()
        board.get_key()


def main(stdscr):
    locale.setlocale(locale.LC_ALL, 'C')
    keyloop(stdscr)

if __name__ == '__main__':
    curses.wrapper(main)
