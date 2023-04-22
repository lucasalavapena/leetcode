class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        f = [nums[0], max(nums[0], nums[1])]
        n = len(nums)
        for i in range(2, n):
            f[i % 2] = max(nums[i] + f[(i - 2) %2 ], f[(i - 1) %2 ]) 
        return f[(n-1) % 2]
        
        