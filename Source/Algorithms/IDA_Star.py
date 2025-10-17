from Utils.utils import find_nearest_food, Manhattan, DDX, isValid


def IDA_Star(_map, _food_Position, start_row, start_col, N, M):
    [food_row, food_col, _id] = find_nearest_food(_food_Position, start_row, start_col)
    if _id == -1:
        return []

    start = (start_row, start_col)
    goal = (food_row, food_col)

    MAX_NODES = 200000

    def dfs(path, g, bound, visited_set, best_g, node_counter):
        node = path[-1]
        h = Manhattan(node[0], node[1], goal[0], goal[1])
        f = g + h

        if f > bound:
            return f, None

        if node == goal:
            return f, path[:]

        prev_best = best_g.get(node)
        if prev_best is None or g < prev_best:
            best_g[node] = g
        else:
            return float('inf'), None

        if node_counter > MAX_NODES:
            return float('inf'), None

        min_over = float('inf')

        # Order neighbors by heuristic (prefer those closer to goal)
        neighbors = []
        for dr, dc in DDX:
            nr, nc = node[0] + dr, node[1] + dc
            if not isValid(_map, nr, nc, N, M) or (nr, nc) in visited_set:
                continue
            nh = Manhattan(nr, nc, goal[0], goal[1])
            neighbors.append((nh, nr, nc))
        neighbors.sort()

        for _, nr, nc in neighbors:
            visited_set.add((nr, nc))
            path.append((nr, nc))
            node_counter += 1
            t, result_path = dfs(path, g + 1, bound, visited_set, best_g, node_counter)
            if result_path is not None:
                return t, result_path
            if t < min_over:
                min_over = t
            path.pop()
            visited_set.remove((nr, nc))

        return min_over, None

    bound = Manhattan(start_row, start_col, food_row, food_col)
    while True:
        path = [start]
        visited_set = {start}
        best_g = {}
        node_counter = 0
        t, res = dfs(path, 0, bound, visited_set, best_g, node_counter)
        if res is not None:
            return [[r, c] for (r, c) in res]
        if t == float('inf'):
            return []

        bound = t
