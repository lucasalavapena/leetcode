class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reference = {0: -1}
        total = 0
        
        for i, n in enumerate(nums):
            total = (total + n) % k
            
            if total not in reference:
                reference[total] = i
            else:
                if i - reference[total] >= 2:
                    return True
        return False
        
        
        
        