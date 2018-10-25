import random


class Actor(object):
    def make_move(self, valid, board):
        raise NotImplementedError

    def pick_board(self, valid, board):
        raise NotImplementedError


class RandomActor(Actor):
    def make_move(self, valid, board):
        while True:
            i = random.randrange(3)
            j = random.randrange(3)
            if valid(i, j):
                return i, j

    def pick_board(self, valid, board):
        while True:
            i = random.randrange(3)
            j = random.randrange(3)
            if valid(i, j):
                return i, j

