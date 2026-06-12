"""Solve the 8-puzzle with A* and the Manhattan-distance heuristic."""
from __future__ import annotations

import heapq
from typing import Dict, List, Optional, Tuple

State = Tuple[int, ...]
GOAL: State = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def manhattan(state: State, goal: State = GOAL) -> int:
    """Sum of Manhattan distances of each tile from its goal position."""
    goal_index = {tile: i for i, tile in enumerate(goal)}
    total = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        g = goal_index[tile]
        total += abs(i // 3 - g // 3) + abs(i % 3 - g % 3)
    return total


def _neighbours(state: State):
    blank = state.index(0)
    row, col = divmod(blank, 3)
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            swap = nr * 3 + nc
            new = list(state)
            new[blank], new[swap] = new[swap], new[blank]
            yield tuple(new)


def is_solvable(state: State) -> bool:
    """Return ``True`` if ``state`` can reach the goal (even inversion parity)."""
    tiles = [t for t in state if t != 0]
    inversions = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1
    return inversions % 2 == 0


def solve(start: State, goal: State = GOAL) -> Optional[List[State]]:
    """Return the shortest sequence of states from ``start`` to ``goal``."""
    if len(start) != 9 or set(start) != set(range(9)):
        raise ValueError("start must be a permutation of 0..8")
    start = tuple(start)
    if not is_solvable(start):
        return None
    if start == goal:
        return [start]
    queue: List[Tuple[int, int, State]] = [(manhattan(start, goal), 0, start)]
    came_from: Dict[State, State] = {}
    g_score: Dict[State, int] = {start: 0}
    counter = 1
    while queue:
        _, _, current = heapq.heappop(queue)
        if current == goal:
            path = [current]
            while path[-1] in came_from:
                path.append(came_from[path[-1]])
            path.reverse()
            return path
        for nb in _neighbours(current):
            tentative = g_score[current] + 1
            if tentative < g_score.get(nb, 10**9):
                g_score[nb] = tentative
                came_from[nb] = current
                heapq.heappush(queue, (tentative + manhattan(nb, goal), counter, nb))
                counter += 1
    return None
