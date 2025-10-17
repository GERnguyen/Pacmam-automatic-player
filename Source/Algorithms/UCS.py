import heapq
from Utils.utils import isValid, DDX, find_nearest_food
from constants import WALL


def UCS(_map, _food_Position, start_row, start_col, N, M, visited_count=None):
	[food_row, food_col, _id] = find_nearest_food(_food_Position, start_row, start_col)
	if _id == -1:
		return []

	heap = []
	heapq.heappush(heap, (0, start_row, start_col))

	dist = [[float('inf') for _ in range(M)] for _ in range(N)]
	dist[start_row][start_col] = 0

	parent = [[None for _ in range(M)] for _ in range(N)]

	while heap:
		cost_so_far, row, col = heapq.heappop(heap)

		if cost_so_far > dist[row][col]:
			continue

		if [row, col] == [food_row, food_col]:
			path = [[food_row, food_col]]
			r, c = food_row, food_col
			while parent[r][c] is not None:
				r, c = parent[r][c]
				path.insert(0, [r, c])
			return path

		for d_r, d_c in DDX:
			nr, nc = row + d_r, col + d_c
			if not isValid(_map, nr, nc, N, M):
				continue
			if _map[nr][nc] == WALL:
				continue

			step_cost = 1
			tie_cost = 0
			if visited_count is not None:
				try:
					tie_cost = 0.01 * visited_count[nr][nc]
				except Exception:
					tie_cost = 0

			new_cost = cost_so_far + step_cost + tie_cost
			if new_cost < dist[nr][nc]:
				dist[nr][nc] = new_cost
				parent[nr][nc] = (row, col)
				heapq.heappush(heap, (new_cost, nr, nc))
				
	return []
