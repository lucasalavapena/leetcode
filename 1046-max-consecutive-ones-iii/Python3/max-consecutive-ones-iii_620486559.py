from collections import deque

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        q = deque()
        max_range = 0
        start = 0
        for i, n in enumerate(nums):
            if len(q) >= k and n == 0:
                max_range = max(i - start, max_range)
                if k != 0:
                    old_idx = q.popleft()
                    start = old_idx + 1
                else:
                    start = i + 1
            if n == 0:
                q.append(i)
            
            if i == len(nums) - 1 and (n != 0 or len(q) <= k):
                max_range = max(i + 1 - start, max_range)
                
        return max_range
                
                
        