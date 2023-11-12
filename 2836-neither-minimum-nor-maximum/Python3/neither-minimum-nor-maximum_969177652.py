class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        welp = set(nums) - set([max(nums), min(nums)])
        return welp.pop() if welp else -1