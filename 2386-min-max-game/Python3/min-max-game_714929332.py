class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while (N := len(nums)) > 1:            
            nums = [max(nums[i], nums[i + 1]) if (i // 2) % 2 else min(nums[i], nums[i + 1])  for i in range(0, N-1, 2)]
            # print(nums)
        return nums[0]