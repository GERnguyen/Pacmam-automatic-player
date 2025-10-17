from Utils.utils import find_nearest_food, DDX, isValid


def IDS(_map, _food_Position, start_row, start_col, N, M):
    [food_row, food_col, _id] = find_nearest_food(_food_Position, start_row, start_col)

    if _id == -1:
        return []

    max_limit = N * M

    for limit in range(max_limit + 1):
        visited = [[False for _ in range(M)] for _ in range(N)]
        trace = [[[-1, -1] for _ in range(M)] for _ in range(N)]

        stack = []
        visited[start_row][start_col] = True
        stack.append([start_row, start_col, 0])

        found = False
        while len(stack) > 0:
            row, col, depth = stack.pop()

            if [row, col] == [food_row, food_col]:
                found = True
                break

            if depth == limit:
                continue

            for [d_r, d_c] in DDX:
                new_row, new_col = row + d_r, col + d_c
                if isValid(_map, new_row, new_col, N, M) and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    trace[new_row][new_col] = [row, col]
                    stack.append([new_row, new_col, depth + 1])

        if found:
            result = [[food_row, food_col]]
            [r, c] = trace[food_row][food_col]
            while r != -1:
                result.insert(0, [r, c])
                [r, c] = trace[r][c]

            return result

    _food_Position.pop(_id)
    return IDS(_map, _food_Position, start_row, start_col, N, M)
