class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c):

            # Check bounds and water
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            # Explore four directions
            dfs(r-1, c)  # up
            dfs(r+1, c)  # down
            dfs(r, c-1)  # left
            dfs(r, c+1)  # right
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    num_of_islands += 1
                    dfs(r, c)  # Start DFS to mark the whole island

        return num_of_islands

        
            