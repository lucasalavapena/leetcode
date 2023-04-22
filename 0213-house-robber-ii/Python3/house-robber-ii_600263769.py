class Solution:
    
    def rob(self, nums: List[int]) -> int:
        a = b = c = d = 0
        for i in range(len(nums)-1):
            a, b = b, max(b, a + nums[i])
            c, d = d, max(d, c + nums[i+1])
        
        return max(b, d, nums[0])