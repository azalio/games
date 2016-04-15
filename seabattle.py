#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
import sys

SIZE = 5


def generate_battle_field():
    field = [[0 for x in xrange(SIZE)] for y in xrange(SIZE)]
    field[randint(0, 4)][randint(0, 4)] = 1
    return field


def get_point():
    try:
        x, y = raw_input("Please, enter two point from 0 to " +
                         str(SIZE - 1) + ":").split()
        x = int(x)
        y = int(y)
        if x >= SIZE or y >= SIZE:
            get_point()
        return [x, y]
    except ValueError:
        get_point()
    except (EOFError, KeyboardInterrupt):
        print "\nBye!"
        sys.exit(0)


if __name__ == "__main__":
    field = generate_battle_field()
    print field
    x, y = get_point()

    while field[x][y] != 1:
        print "you guessed wrong"
        x, y = get_point()
    else:
        print "You are lucky!"
