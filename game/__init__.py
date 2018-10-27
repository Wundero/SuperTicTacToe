import random

from game.actor import RandomActor, Player
from game.board import BigBoard
from game.pray_minimax import MM

cur_player = 1
game_board = BigBoard()


def get_state_string(state, i=-1, k=-1):
    if state < 0:
        return "O"
    if state > 0:
        return "X"
    return "-"


def render():
    for i in range(3):
        for j in range(3):
            for k in range(3):
                ikboard = game_board.get_board(i, k)
                if ikboard.solved() != 0:
                    if j == 1:
                        print("  " + get_state_string(ikboard.solved()) + "   ", end=' ')
                    else:
                        print("      ", end=' ')
                elif ikboard.full():
                    if j == 1:
                        print("  " + "-" + "   ", end=' ')
                    else:
                        print("      ", end=' ')
                else:
                    for l in range(3):
                        print(get_state_string(ikboard.get_cell(j, l), i, k), end=' ')
                print(" ", end='')
            print()
        print()


def select_board(i, j):
    game_board.pick_board(i, j)


def make_move(i, j):
    global cur_player
    global game_board
    if game_board.has_active_board():
        if game_board.play(i, j):
            cur_player *= -1
            if game_board.get_active_board().solved():
                return 1
            else:
                return 0
        else:
            return -1
    else:
        return -1


def main():
    global cur_player
    global game_board
    render()
    r1 = MM()
    r2 = RandomActor()

    actors = [r1, r2]

    while game_board.solved() == 0 and not game_board.full():
        pl = cur_player
        print("Player", get_state_string(cur_player), "turn!")
        if pl < 0:
            pl = 1
        else:
            pl = 0
        act = actors[pl]
        x, y, i, j = act.make_move(game_board)
        if x == -1 or y == -1 or i == -1 or j == -1:
            game_board.change_player()
            cur_player *= -1
            print("skip", x, y, i, j)
            continue  # skip turn, shouldnt happen tho
        print("move:", x, y, i, j)
        select_board(x, y)
        print("k")
        response = make_move(i, j)
        print("l")
        select_board(i, j)
        print('m')
        if game_board.get_active_board().solved() != 0:
            game_board.pick_board(-1, -1)
        print("---------\n")
        render()

    print()
    if game_board.solved() == 0:
        print("The game drew!")
        return
    print(get_state_string(game_board.solved()), "has won!")
    return


main()
