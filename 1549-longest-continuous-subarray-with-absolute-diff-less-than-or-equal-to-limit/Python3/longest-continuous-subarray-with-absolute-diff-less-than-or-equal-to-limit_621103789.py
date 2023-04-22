import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        max_size = 0
        start = 0
        
        min_h = []
        max_h = []

        for i, n in enumerate(nums):
            heapq.heappush(min_h, [n, i])
            heapq.heappush(max_h, [-n, i])
            
            while -max_h[0][0] - min_h[0][0] > limit:
                if min_h[0][1] < max_h[0][1]:
                    val = heapq.heappop(min_h)
                else:
                    val = heapq.heappop(max_h)
                start = max(val[1] + 1, start)
                           
            max_size = max(max_size, i-start + 1)

        return max_size
        