#!/usr/bin/env python

import curses
import locale
import time
from random import randint


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

        curses.noecho()
        curses.cbreak()
        self.scr.keypad(1)

        border_line = '+'+(self.X*'-')+'+'
        self.scr.addstr(0, 0, border_line)
        self.scr.addstr(self.Y+1, 0, border_line)
        for y in range(0, self.Y):
            self.scr.addstr(1+y, 0, '|')
            self.scr.addstr(1+y, self.X+1, '|')
        self.scr.refresh()

        border_line = '+'+((self.X-6)*'-')+'+'
        self.scr.addstr(3, 3, border_line)
        self.scr.addstr(self.Y-1, 3, border_line)
        for y in range(3, self.Y):
            self.scr.addstr(y, 3, '|')
            self.scr.addstr(y, self.X-2, '|')
        self.scr.refresh()

    def generate_balls(self, number_of_balls=1):
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
            if y+1 > self.Y:
                if z == 3:
                    z = 7
                elif z == 4:
                    z = 0
                elif z == 5:
                    z = 1
            if y-1 < 4:
                if z == 0:
                    z = 4
                elif z == 1:
                    z = 5
                elif z == 7:
                    z = 3
            if x+1 > self.X-7:
                if z == 1:
                    z = 5
                elif z == 2:
                    z = 6
                elif z == 3:
                    z = 7
            if x-1 < 4:
                if z == 5:
                    z = 1
                elif z == 6:
                    z = 2
                elif z == 7:
                    z = 3

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
        time.sleep(0.3)
        board.game_run()
        pass


def main(stdscr):
    locale.setlocale(locale.LC_ALL, '')
    keyloop(stdscr)

if __name__ == '__main__':
    curses.wrapper(main)
