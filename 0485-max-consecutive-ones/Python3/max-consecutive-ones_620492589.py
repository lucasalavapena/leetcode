class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        start = -1
        max_cons = 0
        
        for i, n in enumerate(nums):
            if n == 0:
                start = i
            elif n == 1:
                max_cons = max(max_cons, i-start)
        
        return max_cons