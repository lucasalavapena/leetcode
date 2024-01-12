class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return max([(x**2 + y**2, x * y) for x, y in dimensions])[1]