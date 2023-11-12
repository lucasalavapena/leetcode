class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for r in grid:
            r.sort()
        return sum(max(r) for r in zip(*grid))