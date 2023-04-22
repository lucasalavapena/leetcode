class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        nsorted_nums = sorted(nums)
        
        return nums.index(nsorted_nums[-1]) if nsorted_nums[-1] >= 2 * nsorted_nums[-2] else -1