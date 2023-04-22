from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        q = collections.deque()
        out = []
        prev_max = float("-inf")
        for i, n in enumerate(nums):
            while q and nums[q[-1]] < n:
                q.pop()
            
            q.append(i)
                        
            if q[0] == i - k:
                q.popleft()
                
            if i + 1 >= k:
                out.append(nums[q[0]])
     

        return out
