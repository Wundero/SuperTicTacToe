import random


class Actor(object):
    def make_move(self, valid, board):
        raise NotImplementedError

    def pick_board(self, valid, board):
        raise NotImplementedError


class Player(Actor):
    def make_move(self, valid, board):
        while True:
            coords = tuple(map(int, input().split(',')))
            if valid(coords[0], coords[1]):
                return coords

    def pick_board(self, valid, board):
        while True:
            coords = tuple(map(int, input().split(',')))
            if valid(coords[0], coords[1]):
                return coords


class RandomActor(Actor):
    def make_move(self, valid, board):
        for x in range(100):
            i = random.randrange(3)
            j = random.randrange(3)
            if valid(i, j):
                return i, j
        for i in range(3):
            for j in range(3):
                if valid(i, j):
                    return i, j
        return -1, -1

    def pick_board(self, valid, board):
        for x in range(100):
            i = random.randrange(3)
            j = random.randrange(3)
            if valid(i, j):
                return i, j
        for i in range(3):
            for j in range(3):
                if valid(i, j):
                    return i, j
        return -1, -1
