import math

class Solution:
    def computeScore(self, piles, h, k):
        time_taken = 0
        for p in piles:
            time_taken += math.ceil(p/k)
            
        return time_taken <= h
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        while l <= r:
            mid = (l + r)//2
          
            if self.computeScore(piles, h, mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l
            
            
                