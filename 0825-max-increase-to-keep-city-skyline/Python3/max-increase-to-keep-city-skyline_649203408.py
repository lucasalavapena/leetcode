class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        rows = [0] * m
        cols = [0] * n
        
        for i in range(m):
            for j in range(n):
                rows[i] = max(rows[i], grid[i][j])
                cols[j] = max(cols[j], grid[i][j])
        res = 0
        for i in range(m):
            for j in range(n):
                res += max(min(rows[i], cols[j]), grid[i][j]) - grid[i][j]
        return res