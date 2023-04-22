class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res = nums[:]
        
        while len(res) >= 2:
            res = [(res[i] + res[i + 1]) % 10 for i in range(len(res)-1)]
            
        return res[0]