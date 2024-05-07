def numIslands(grid):
    def dfs(grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'  # Mark the current cell as visited
        # Visit adjacent cells
        dfs(grid, i+1, j)
        dfs(grid, i-1, j)
        dfs(grid, i, j+1)
        dfs(grid, i, j-1)

    if not grid:
        return 0

    num_islands = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                num_islands += 1
                dfs(grid, i, j)

    return num_islands

# Example usage:
grid1 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
print(numIslands(grid1))  # Output: 1

grid2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(numIslands(grid2))  #
