from Utils.utils import DDX, isValid2
from constants import FOOD, MONSTER, WALL
from Algorithms.LocalSearch import calc_heuristic
from queue import PriorityQueue
import random
import heapq

class BeamPriorityQueue:
    def __init__(self, beam_width):
        self.beam_width = beam_width
        self.heap = [] 

    def push(self, priority, item):
        if len(self.heap) < self.beam_width:
            heapq.heappush(self.heap, (-priority, item))
        else:
            if -priority > self.heap[0][0]: 
                heapq.heapreplace(self.heap, (-priority, item))


def BeamSearch(_map, start_row, start_col, N, M, _visited):
    visited = []
    cost = [[0 for _ in range(M)] for _ in range(N)]

    calc_heuristic(_map, start_row, start_col, start_row, start_col, N, M, 3, visited, cost, _visited)

    start = (start_row, start_col)
    path = [[], []]
    result = []
    trace = {}
    beam_width = 2
    beam = BeamPriorityQueue(beam_width=beam_width)
    level_queue = []
    level_queue.append(start)


    for _ in range(3):
        while level_queue:
            (start_row, start_col) = level_queue.pop()
            neighbors = DDX.copy()
            random.shuffle(neighbors)
            for [d_r, d_c] in neighbors:
                new_row, new_col = start_row + d_r, start_col + d_c
                actualCost = cost[new_row][new_col] - _visited[new_row][new_col]
                if _map[new_row][new_col] != WALL:
                    result = (new_row, new_col)
                    beam.push(-actualCost, result)
                    trace[result] = (start_row, start_col)


        for i in range(len(beam.heap)):        
            _, gr = beam.heap.pop()
            level_queue.append(gr)
            path[i].append(gr)
        

    if cost[path[0][-1][0]][path[0][-1][1]] >= cost[path[1][-1][0]][path[1][-1][1]]:
        print(path[0])
        return path[0]
    else:
        print(path[1])
        return path[1]

