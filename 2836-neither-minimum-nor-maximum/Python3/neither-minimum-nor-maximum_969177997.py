class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        return (set(nums) - set([max(nums), min(nums)])).pop() if len(nums) > 2 else -1