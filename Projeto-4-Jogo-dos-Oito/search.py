from collections import deque
from eight_puzzle import EightPuzzle, GOAL_STATE
import heapq
from itertools import count

def bfs(start):
    queue = deque()
    queue.append((start, []))
    visited = set()
    visited.add(str(start.state))

    while queue:
        current, path = queue.popleft()
        if current.is_goal():
            return path
        for move in current.possible_moves():
            next_state = current.move(move)
            if next_state and str(next_state.state) not in visited:
                visited.add(str(next_state.state))
                queue.append((next_state, path + [move]))
    return None

def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                for x in range(3):
                    for y in range(3):
                        if GOAL_STATE[x][y] == value:
                            distance += abs(x - i) + abs(y - j)
    return distance

def astar(start):
    heap = []
    counter = count()
    heapq.heappush(heap, (manhattan(start.state), 0, next(counter), start, []))
    visited = set()
    visited.add(str(start.state))

    while heap:
        est_total, cost, _, current, path = heapq.heappop(heap)
        if current.is_goal():
            return path
        for move in current.possible_moves():
            next_state = current.move(move)
            if next_state and str(next_state.state) not in visited:
                visited.add(str(next_state.state))
                g = cost + 1
                h = manhattan(next_state.state)
                heapq.heappush(heap, (g + h, g, next(counter), next_state, path + [move]))
    return None