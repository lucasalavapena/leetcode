class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        N = len(grid)
        champion = 0
        for j in range(1, N):
            if grid[champion][j] == 0:
                champion = j

        return champion