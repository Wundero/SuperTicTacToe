from game.actor import Actor


class MM(Actor):
    step = 0

    def make_move(self, board):
        return self.minimax(board)

    def get_depth(self, board):
        zeros = board.zeros()
        if zeros > 22:
            return 2
        if zeros > 10:
            return 3
        if zeros > 6:
            return 4
        return 5

    def minimax(self, board):
        self.step = 0
        actions = board.actions()
        if len(actions) == 0:
            return -1, -1, -1, -1
        best_action = actions[0]
        best_score = float('-inf')
        for action in actions:
            next_state = board.simulate(action)
            score = self.min_play(next_state, self.get_depth(board))
            if score > best_score:
                best_action = action
                best_score = score
        return best_action

    def min_play(self, state, depth):
        self.step += 1
        if state.solved() != 0:
            return self.evaluate(state)
        moves = state.actions()
        best_score = float('inf')
        for move in moves:
            other = state.simulate(move)
            score = float('inf')
            if depth > 0:
                score = self.max_play(other, depth - 1)
            else:
                score = other.score()
            if score < best_score:
                best_score = score
        return best_score

    def max_play(self, state, depth):
        self.step += 1
        if state.solved() != 0:
            return self.evaluate(state)
        moves = state.actions()
        best_score = float('-inf')
        for move in moves:
            other = state.simulate(move)
            score = float('-inf')
            if depth > 0:
                score = self.min_play(other, depth - 1)
            else:
                score = other.score()
            if score > best_score:
                best_score = score
        return best_score

    def evaluate(self, state):
        return float('inf') * state.solved()
