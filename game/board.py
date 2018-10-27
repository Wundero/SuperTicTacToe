import copy


class Board(object):

    def __init__(self, bid):
        self.bid = bid
        self.my_cells = [[0 for y in range(3)] for x in range(3)]

    def get_cell(self, i: int, j: int):
        return self.my_cells[i][j]

    def set_cell(self, i: int, j: int, state):
        self.my_cells[i][j] = state

    def full(self):
        for i in range(3):
            for j in range(3):
                if self.get_cell(i, j) == 0:
                    return False
        return True

    def zeros(self):
        out = 0
        for i in range(3):
            for j in range(3):
                if self.get_cell(i, j) == 0:
                    out += 1
        return out

    def three_score(self, a, b, c):
        return self.get_cell(a[0], a[1]) + self.get_cell(b[0], b[1]) + self.get_cell(c[0], c[1])

    def three_solved(self, a, b, c):
        num = self.three_score(a, b, c)
        if num == 3:
            return 1
        elif num == -3:
            return -1
        else:
            return 0

    def solved(self):
        rows = [[[], [], []], [[], [], []], [[], [], []]]
        for i in range(3):
            for j in range(3):
                rows[i][j] = (i, j)
        cols = [[[], [], []], [[], [], []], [[], [], []]]
        for i in range(3):
            for j in range(3):
                cols[i][j] = (j, i)
        diags = [[(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]]
        for row in rows:
            val = self.three_solved(row[0], row[1], row[2])
            if val != 0:
                return val
        for row in cols:
            val = self.three_solved(row[0], row[1], row[2])
            if val != 0:
                return val
        for row in diags:
            val = self.three_solved(row[0], row[1], row[2])
            if val != 0:
                return val
        return 0


class BigBoard(object):

    def __init__(self):
        self.boards = ((Board(0), Board(1), Board(2)),
                       (Board(3), Board(4), Board(5)),
                       (Board(6), Board(7), Board(8)))
        self.activeBoard = [-1, -1]
        self.activePlayer = 1

    def zeros(self):
        out = 0
        for i in range(3):
            for j in range(3):
                out += self.get_board(i, j).zeros()
        return out

    def actions(self):
        if self.has_active_board():
            out = []
            for i in range(3):
                for j in range(3):
                    if self.is_move_valid(i, j):
                        out.append((self.activeBoard[0], self.activeBoard[1], i, j))
            return out
        else:
            out = []
            for i in range(3):
                for j in range(3):
                    if self.is_board_valid(i, j):
                        for k in range(3):
                            for l in range(3):
                                if self.get_board(i, j).get_cell(k, l) == 0:
                                    out.append((i, j, k, l))
            return out

    def simulate(self, action):
        other = copy.deepcopy(self)
        other.action(action)
        return other

    def change_player(self):
        self.activePlayer *= -1

    def three_score(self, a, b, c):
        return self.get_board(a[0], a[1]).solved() \
               + self.get_board(b[0], b[1]).solved() \
               + self.get_board(c[0], c[1]).solved()

    def score(self):
        rows = [[[], [], []], [[], [], []], [[], [], []]]
        for i in range(3):
            for j in range(3):
                rows[i][j] = (i, j)
        cols = [[[], [], []], [[], [], []], [[], [], []]]
        for i in range(3):
            for j in range(3):
                cols[i][j] = (j, i)
        diags = [[(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]]
        val = 0
        for row in rows:
            val += self.three_score(row[0], row[1], row[2])
        for row in cols:
            val += self.three_score(row[0], row[1], row[2])
        for row in diags:
            val += self.three_score(row[0], row[1], row[2])
        return val * self.activePlayer

    def three_solved(self, a, b, c):
        num = self.three_score(a, b, c)
        if num == 3:
            return 1
        elif num == -3:
            return -1
        else:
            return 0

    def full(self):
        for i in range(3):
            for j in range(3):
                if not self.get_board(i, j).full() and not self.get_board(i, j).solved():
                    return False
        return True

    def solved(self):
        rows = [[[], [], []], [[], [], []], [[], [], []]]
        for i in range(3):
            for j in range(3):
                rows[i][j] = (i, j)
        cols = [[[], [], []], [[], [], []], [[], [], []]]
        for i in range(3):
            for j in range(3):
                cols[i][j] = (j, i)
        diags = [[(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]]
        for row in rows:
            val = self.three_solved(row[0], row[1], row[2])
            if val != 0:
                return val
        for row in cols:
            val = self.three_solved(row[0], row[1], row[2])
            if val != 0:
                return val
        for row in diags:
            val = self.three_solved(row[0], row[1], row[2])
            if val != 0:
                return val
        return 0

    def pick_board(self, i: int, j: int):
        self.activeBoard[0] = i
        self.activeBoard[1] = j

    def has_active_board(self):
        return self.activeBoard[0] >= 0

    def play(self, i, j):
        if self.get_active_board().get_cell(i, j) != 0:
            return False
        self.get_active_board().set_cell(i, j, self.activePlayer)
        self.activePlayer *= -1
        return True

    def action(self, action):
        self.pick_board(action[0], action[1])
        self.play(action[2], action[3])

    def get_active_coords(self):
        return self.activeBoard

    def get_active_board(self):
        if self.is_in_range(self.activeBoard[0], self.activeBoard[1]):
            return self.get_board(self.activeBoard[0], self.activeBoard[1])
        return None

    @staticmethod
    def is_in_range(i, j):
        return 0 <= i < 3 and 0 <= j < 3

    def get_board(self, i, j):
        if self.is_in_range(i, j):
            return self.boards[i][j]
        return None

    def is_board_valid(self, i, j):
        return self.is_in_range(i, j) \
               and self.get_board(i, j).solved() == 0 \
               and not self.get_board(i, j).full()

    def is_move_valid(self, i, j, x=-1, y=-1):
        ab = self.get_board(x, y)
        if ab is None:
            ab = self.get_active_board()
        if ab is None:
            return False
        return self.is_in_range(i, j) and ab.get_cell(i, j) == 0
