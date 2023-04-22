class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_count = 1
        N = len(nums)
        l, r = 0, 0
        total = 0

        while r < N:
            total += nums[r]
            
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            max_count = max(max_count, r - l + 1)
            r += 1
            
            
        return max_count