class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        def dfs(i, j, gold):
            if 0 <= i < M and 0 <= j < N and grid[i][j]:
                curr_gold, grid[i][j] = grid[i][j], 0
                gold = max(dfs(x, y, gold+curr_gold) for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)))
                grid[i][j] = curr_gold
            return gold
        return max(dfs(i, j, 0) for i in range(M) for j in range(N))