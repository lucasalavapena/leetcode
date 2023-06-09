class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[-1][-1] == -1: return 0
        
        # set up cache
        self.grid = grid
        self.memo = {}
        self.N = len(grid)
        
        return max(self.dp(0, 0, 0, 0), 0)
    
    # reformulate problem as two people picking up as many cherries as possible
    def dp(self, i1, j1, i2, j2):
        # already stored: return 
        if (i1, j1, i2, j2) in self.memo: return self.memo[(i1, j1, i2, j2)]
        
        # end states: 1. out of grid 2. at the right bottom corner 3. hit a thorn
        N = self.N
        if i1 == N or j1 == N or i2 == N or j2 == N: return -1
        if i1 == N-1 and j1 == N-1 and i2 == N-1 and j2 == N-1: return self.grid[-1][-1]
        if self.grid[i1][j1] == -1 or self.grid[i2][j2] == -1: return -1
        
        # now can take a step in two directions at each end, which amounts to 4 combinations in total
        dd = self.dp(i1 + 1, j1, i2 + 1, j2)
        dr = self.dp(i1 + 1, j1, i2, j2 + 1)
        rd = self.dp(i1, j1 + 1, i2 + 1, j2)
        rr = self.dp(i1, j1 + 1, i2, j2 + 1)
        maxComb = max([dd, dr, rd, rr])
        
        # find if there is a way to reach the end
        if maxComb == -1:
            out = -1
        else:
            # same cell, can only count this cell once
            if i1 == i2 and j1 == j2:
                out = maxComb + self.grid[i1][j1]
            # different cell, can collect both
            else:
                out = maxComb + self.grid[i1][j1] + self.grid[i2][j2]
        
        # no need overwrite grid since they cant come back to it
        
        # cache result
        # note symmetry, if we swap the people it is the same problem
        self.memo[(i1, j1, i2, j2)] = out
        self.memo[(i2, j2, i1, j1)] = out
        return out