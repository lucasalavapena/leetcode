from collections import deque

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for i, n in enumerate(nums):
            k += n - 1
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return i - left +1
                
                
        