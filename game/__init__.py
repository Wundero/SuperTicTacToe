import random

from game.actor import RandomActor
from game.board import BigBoard

cur_player = 1
game_board = BigBoard()


def get_state_string(state, i=-1, k=-1):
    if state < 0:
        return "O"
    if state > 0:
        return "X"
    if i >= 0 and k >= 0:
        num = 3 * i + k
        return str(num)
    return "-"


def render():
    for i in range(3):
        for j in range(3):
            for k in range(3):
                ikboard = game_board.get_board(i, k)
                if ikboard.solved() != 0:
                    if j == 2:
                        print("  " + get_state_string(ikboard.solved()) + "   ", end=' ')
                    else:
                        print("      ", end=' ')
                else:
                    for l in range(3):
                        print(get_state_string(ikboard.get(j, l), i, k), end=' ')
                print(" ", end='')
            print()
        print()


def select_board(i, j):
    game_board.pick_board(i, j)


def make_move(i, j):
    global cur_player
    global game_board
    if game_board.has_active_board():
        if game_board.play(i, j, cur_player):
            cur_player *= -1
            if game_board.get_active_board().solved():
                return 1
            else:
                return 0
        else:
            return -1
    else:
        return -1


def is_board_valid(i, j):
    return game_board.is_in_range(i, j)


def is_move_valid(i, j):
    return game_board.is_in_range(i, j) & game_board.get_active_board().get(i, j) == 0


def main():
    global cur_player
    global game_board
    render()
    r1 = RandomActor()
    r2 = RandomActor()

    actors = [r1, r2]

    while game_board.solved() == 0:
        pl = cur_player
        if pl < 0:
            pl = 1
        else:
            pl = 0
        act = actors[pl]
        print("actor", pl, "selected")
        if not game_board.has_active_board():
            x, y = act.pick_board(is_board_valid, game_board)
            select_board(x, y)
            print("board", x, y, "selected")
        print("active coords:", game_board.get_active_coords())
        i, j = act.make_move(is_move_valid, game_board)
        print("move", i, j, "selected")
        response = make_move(i, j)
        print("move made")
        game_board.pick_board(i, j)
        print("board picked")

        if game_board.get_active_board().solved() != 0:
            game_board.pick_board(-1, -1)
        print("---------\n")
        render()
    print(get_state_string(game_board.solved()), "has won!")


main()
