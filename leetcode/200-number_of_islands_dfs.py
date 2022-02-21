class Solution:
    
    def explore(self, grid, i, j):
        
        R = len(grid)
        C = len(grid[0])
        
        
        grid[i][j] = '0'
        
        explore_points = [[i-1, j], [i, j+1], [i+1, j], [i, j-1]] # 4 directions for horizontally / vertical connected 1's
        for point in explore_points:
            r, c = point[0], point[1]
            if 0 <= r < R and 0 <= c < C and grid[r][c] == '1':
                self.explore(grid, r, c)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        
        R = len(grid)
        C = len(grid[0])
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    self.explore(grid, i, j) # dfs to explore all connected 1's that beling to this island
                    count += 1
        
        return count