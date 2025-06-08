from collections import deque
def bfs_without_teleport(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([(0, 0, 0)])  # (r, c, steps)
    visited.add((0, 0))
    while queue:
        r, c, steps = queue.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return steps
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '0' and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, steps + 1))
    return -1
def bfs_with_teleport(grid):
    rows, cols = len(grid), len(grid[0])
    empty_cells = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == '0']
    visited = set()
    queue = deque([(0, 0, False, 0)])  # (r, c, teleport_used, steps)
    visited.add((0, 0, False))
    while queue:
        r, c, used, steps = queue.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return steps
        # Move normally
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            state = (nr, nc, used)
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '0' and state not in visited:
                visited.add(state)
                queue.append((nr, nc, used, steps + 1))
        # One-time teleport
        if not used:
            for tr, tc in empty_cells:
                if (tr, tc) != (r, c):
                    state = (tr, tc, True)
                    if state not in visited:
                        visited.add(state)
                        queue.append((tr, tc, True, steps + 1))
    return -1
# Sample grid
grid = [
    ['0', '1', '0'],
    ['0', '1', '0'],
    ['0', '0', '0']
]
# Run both versions
steps_without = bfs_without_teleport(grid)
steps_with = bfs_with_teleport(grid)
#  Print results
print("Shortest path WITHOUT teleport:", steps_without)
print("Shortest path WITH teleport:", steps_with)
