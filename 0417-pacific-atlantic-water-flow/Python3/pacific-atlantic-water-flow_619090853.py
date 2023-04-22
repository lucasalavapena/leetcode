class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.rows = len(heights)
        self.columns = len(heights[0])
        self.heights = heights
        
        pacific_visited = set()
        atlantic_visited = set()
        
        for i in range(self.rows):
            self.dfs(i, 0, pacific_visited)
            self.dfs(i, self.columns-1, atlantic_visited)
            
        for i in range(self.columns):
            self.dfs(0, i, pacific_visited)
            self.dfs(self.rows-1, i, atlantic_visited)
        
        intersection = pacific_visited.intersection(atlantic_visited)
        return [list(l) for l in list(intersection)]
        
        
    def dfs(self, r, c, visited):
        
        visited.add((r, c))
        
        for (x, y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_i, new_j = r + x, c + y
            if (new_i, new_j) not in visited and 0 <= new_i < self.rows and 0 <= new_j < self.columns and self.heights[r][c] <= self.heights[new_i][new_j] :
                self.dfs(new_i, new_j, visited)
        
        
        
        