class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        cols = [sum(r[j] for r in grid) for j in range(n)]
        rows =  [sum(r) for r in grid]
        return [[2 * (rows[i] + cols[j]) - n - m  for j in range(n)] for i in range(m)] 