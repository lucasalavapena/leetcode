class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        if len(heights) == 1: return 0
        
        count = 0
        
        sorted_heights = sorted(heights)
        
        for i, v in zip(heights, sorted_heights):
            count += not i == v
        return count