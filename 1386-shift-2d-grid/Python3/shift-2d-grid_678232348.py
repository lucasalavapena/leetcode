class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        required_k = k % (m * n)
        
        for _ in range(required_k):
            res = [g[:] for g in grid]
            
            for i in range(m):
                for j in range(n):
                    if j == n-1:
                        if i == m-1:
                            res[0][0] = grid[i][j]
                        else:
                            res[i + 1][0] = grid[i][j]
                    else:
                        res[i][j + 1] = grid[i][j]
                        
            grid = [r[:] for r in res]
            
        return grid
                        