class Solution:
    def countElements(self, nums: List[int]) -> int:
        lo, hi = min(nums), max(nums)
        return sum(1 for x in nums if lo<x<hi)
            