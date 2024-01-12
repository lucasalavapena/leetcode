class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        diff = [[0] * n for _ in range(m)]
        cols = [sum(r[j] for r in grid) for j in range(n)]
        rows =  [sum(r) for r in grid]
        for i in range(m):
            for j in range(n):
                diff[i][j] = 2 * (rows[i] + cols[j]) - n - m 
        return diff