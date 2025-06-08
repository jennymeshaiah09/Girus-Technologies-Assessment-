def count_islands(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    # 8 directions (including diagonals)
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),     # up, down, left, right
        (-1, -1), (-1, 1), (1, -1), (1, 1)    # diagonals
    ]
    def dfs(r, c):
        stack = [(r, c)]
        size = 0
        while stack:
            x, y = stack.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            size += 1

            for dr, dc in directions:
                nr, nc = x + dr, y + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '1' and not visited[nr][nc]:
                        stack.append((nr, nc))
        return size
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and not visited[i][j]:
                group_size = dfs(i, j)
                if group_size >= 2:  # only count groups with size ≥ 2
                    count += 1

    return count
grid = [
    ['1', '0', '0'],
    ['0', '1', '1'],
    ['0', '0', '1']
]
print("Islands of size ≥2:", count_islands(grid))
