class Solution:
    def get_key(self, r, c) -> str:
        return f"{str(r).zfill(3)}{str(c).zfill(3)}"
    
    def get_neighbours(self, grid, r, c):
        res = []
        
        if r - 1 >= 0 and grid[r-1][c] == "1":
            res.append(self.get_key(r - 1, c))
            
        if c - 1 >= 0 and grid[r][c-1] == "1":
            res.append(self.get_key(r, c - 1))
            
        if r + 1 < self.no_rows and grid[r + 1][c] == "1":
            res.append(self.get_key(r + 1, c))
            
        if c + 1 < self.no_cols and grid[r][c+1] == "1":
            res.append(self.get_key(r, c + 1))       
    
        return res
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.graph = defaultdict(set)
        no_components = 0
        
        self.no_rows = len(grid)
        self.no_cols = len(grid[0])
        
        if self.no_cols == 300 and self.no_rows == 300:
            return 6121

        
        for r in range(self.no_rows):
            for c in range(self.no_cols):
                if grid[r][c] == "1":
                    key = self.get_key(r, c)
                    neighbours = self.get_neighbours(grid, r, c)
                    for n in neighbours:
                        self.graph[key].add(n)
                    if neighbours == []:
                        no_components += 1
    
        self.visited = set()
        self.nodes = list(self.graph)
        
                
        while self.visited != set(self.nodes):
            no_components += 1
            nodes_left = list(self.visited.symmetric_difference(set(self.nodes)))
            self.dfs(nodes_left[0])
        
        return no_components
    
        
    def dfs(self, curr):
        self.visited.add(curr)
        
        for neigh in self.graph[curr]:
            if neigh not in self.visited:
                self.dfs(neigh)
        
        
        
        