class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        size = 0
        res = [0] * len(nums)
        for n in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                
                if res[m] < n:
                    i = m + 1
                else:
                    j = m
                    
            res[i] = n
            size = max(size, i + 1)
            if size > 2: return True
                
            
        return False