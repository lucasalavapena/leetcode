class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        total, i, max_freq = 0, 0, 0
        for j, n in enumerate(nums):
            total += n
            while n * (j - i + 1) > total + k:
                total -= nums[i]
                i += 1
            max_freq = max(max_freq, j - i + 1)
        return max_freq