class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return list(set(nums).symmetric_difference(set(range(len(nums)+1))))[0]