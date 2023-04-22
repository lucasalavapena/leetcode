class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        cnt = 0
        # for row
        for i in range(m):
            cnt += bisect_left(grid[i][::-1], 0)
        return cnt