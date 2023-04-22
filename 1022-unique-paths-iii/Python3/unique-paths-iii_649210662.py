class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0]) 
        start_i, start_j = -1, -1
        self.end_i, self.end_j = -1, -1
        
        # self.forbidden = set()
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for i in range(self.m):
            for j in range(self.n):
                # if grid[i][j] == 0:
                #     forbidden.add((i, j))
                if grid[i][j] == 1:
                    start_i, start_j = i, j
                elif grid[i][j] == 2:
                    self.end_i, self.end_j = i, j
                    
        grid[start_i][start_j] = -1
        self.ways = 0
        self.helper(start_i, start_j, grid)
        return self.ways

    
    def helper(self, i, j, grid):
        if i == self.end_i and j == self.end_j:
            if list(chain(*grid)).count(-1) == self.m * self.n:
                self.ways += 1
            else:
                return
        
        
        for dx, dy in self.directions:
            new_x, new_y = i + dx, j + dy
            
            if  0 <= new_x < self.m and 0 <= new_y < self.n and grid[new_x][new_y] != -1:
                tmp = grid[new_x][new_y]
                grid[new_x][new_y] = -1
                
                self.helper(new_x, new_y, grid)
                
                grid[new_x][new_y] = tmp
                
                
                
                
                