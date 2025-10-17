from Utils.utils import DDX, isValid2
from constants import FOOD, MONSTER, WALL
from Algorithms.LocalSearch import calc_heuristic
import random

def simulatedAnnealing(_map, start_row, start_col, N, M, _visited):
    visited = []
    cost = [[0 for _ in range(M)] for _ in range(N)]

    calc_heuristic(_map, start_row, start_col, start_row, start_col, N, M, 3, visited, cost, _visited)

    max_f = cost[start_row][start_col] - _visited[start_row][start_col]

    path = []
    result = []

    T = 100
    for i in range(3):
        max_local = float("-inf")
        neighbors = DDX.copy()
        random.shuffle(neighbors)
        for [d_r, d_c] in neighbors:
            new_row, new_col = start_row + d_r, start_col + d_c
            actualCost = cost[new_row][new_col] - _visited[new_row][new_col]
            if actualCost > max_local and _map[new_row][new_col] != WALL:
                max_local = actualCost
                result = [new_row, new_col]
        if max_local <= max_f:
            alpha = (cost[new_row][new_col] - _visited[new_row][new_col]) - (cost[start_row][start_col] - _visited[start_row][start_col])
            p = 2.71828 ** (alpha / T)
            r = random.uniform(0, 1)
            if r > p: return path
        max_f = max_local
        start_row, start_col = result[0], result[1]
        path.append(result)
        T -= 30

    return path
    
