class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        return int((len(nums) / 2) * (1 + len(nums))) - sum(nums)
        # return numbers[0]