class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        a = set(range(1, (N**2) +1))
        flat = [grid[i][j] for i in range(N) for j in range(N)]
        b = set(flat)
        return [Counter(flat).most_common(1)[0][0], max(a-b)]
        