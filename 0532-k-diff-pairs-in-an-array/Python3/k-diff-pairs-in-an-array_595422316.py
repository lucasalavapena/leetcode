class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        if len(nums) == 1:
            return 0
        
        res = set()
        nums.sort()
        
        count = 0
        i, j = 0, 1
        
        while (i < len(nums) - 1):   
            if (nums[j] - nums[i] == k):
                res.add((nums[i], nums[j]))
                i+= 1
                j += 1
            else:
                j += 1
                
            if (j == len(nums)):
                i += 1
                j = i + 1
                
        return len(res)
        
        