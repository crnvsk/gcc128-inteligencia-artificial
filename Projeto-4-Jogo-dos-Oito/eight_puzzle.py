import copy
import random

GOAL_STATE = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

class EightPuzzle:
    def __init__(self, state):
        self.state = state

    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def is_goal(self):
        return self.state == GOAL_STATE

    def possible_moves(self):
        moves = []
        i, j = self.find_zero()
        directions = {
            'Cima': (i-1, j),
            'Baixo': (i+1, j),
            'Esquerda': (i, j-1),
            'Direita': (i, j+1)
        }
        for move, (new_i, new_j) in directions.items():
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                moves.append(move)
        return moves

    def move(self, direction):
        i, j = self.find_zero()
        new_state = copy.deepcopy(self.state)
        if direction == 'Cima' and i > 0:
            new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        elif direction == 'Baixo' and i < 2:
            new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
        elif direction == 'Esquerda' and j > 0:
            new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
        elif direction == 'Direita' and j < 2:
            new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
        else:
            return None
        return EightPuzzle(new_state)

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

def generate_random_state(moves=50):
        puzzle = EightPuzzle([row[:] for row in GOAL_STATE])
        for _ in range(moves):
            possiveis = puzzle.possible_moves()
            move = random.choice(possiveis)
            puzzle = puzzle.move(move)
        return puzzle.state