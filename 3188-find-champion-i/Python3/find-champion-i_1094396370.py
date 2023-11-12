class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i, line in enumerate(grid): 
            if line.count(1) == n-1:
                return i