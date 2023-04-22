class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(heights[i] != h for i, h in enumerate(sorted(heights)))