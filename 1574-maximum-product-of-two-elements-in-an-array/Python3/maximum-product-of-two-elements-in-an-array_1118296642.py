class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1, max2 = min(nums[0], nums[1]), max(nums[0], nums[1])
        for i in range(2, len(nums)):
            if max2 < nums[i]:
                max1 = max2
                max2 = nums[i]
            elif max1 < nums[i]: 
                max1 = nums[i]
        return (max1-1) * (max2-1)