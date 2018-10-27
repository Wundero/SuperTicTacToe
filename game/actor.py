import random


class Actor(object):
    def make_move(self, board):
        raise NotImplementedError


class Player(Actor):

    def make_move(self, board):
        while True:
            coords = tuple(map(int, input().split(',')))
            if board.has_active_board():
                if board.is_move_valid(coords[0], coords[1]):
                    return board.get_active_coords()[0], board.get_active_coords()[1], coords[0], coords[1]
                else:
                    print("reenter")
            if board.is_board_valid(coords[0], coords[1]) and board.is_move_valid(coords[2], coords[3]):
                return coords
            else:
                print("reenter")


class RandomActor(Actor):

    def pick_not_random(self, board):
        for k in range(3):
            for l in range(3):
                if board.is_board_valid(i, j):
                    return k, l

    def make_move(self, board):
        x = -1
        y = -1
        i = 0
        j = 0
        if not board.has_active_board():
            for f in range(100):
                x = random.randrange(3)
                y = random.randrange(3)
                if board.is_board_valid(x, y):
                    break
        else:
            x = board.get_active_coords()[0]
            y = board.get_active_coords()[1]

        if x == -1 and y == -1:
            for k in range(3):
                for l in range(3):
                    if board.is_board_valid(i, j):
                        x = k
                        y = l

        for f in range(100):
            i = random.randrange(3)
            j = random.randrange(3)
            if board.is_move_valid(i, j, x, y):
                return x, y, i, j
        for i in range(3):
            for j in range(3):
                if board.is_move_valid(i, j, x, y):
                    return x, y, i, j
        print(x, y, i, j)
        return -1, -1, -1, -1
