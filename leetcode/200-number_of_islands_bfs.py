class Solution:
    
    def bfs(self, grid, row, col):
        grid[row][col] = '0'
        queue = collections.deque([(row, col)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 4 directions for horizontally / vertical connected 1's

        R = len(grid)
        C = len(grid[0])

        while len(queue) > 0:
            (i, j) = queue.popleft()
            
            for d in directions:
                next_i, next_j = i +d[0], j + d[1]
                if 0 <= next_i < R and 0 <= next_j< C and grid[next_i][next_j] == '1':
                    grid[next_i][next_j] = '0' # making it a 0 so that we keep tracks of cells that have been explored
                    queue.append((next_i, next_j))
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        
        R = len(grid)
        C = len(grid[0])
        
        # traversing the entire grid
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    count += 1
                    self.bfs(grid, i, j) # bfs to explore all connected 1's that beling to this island
                    

        return count