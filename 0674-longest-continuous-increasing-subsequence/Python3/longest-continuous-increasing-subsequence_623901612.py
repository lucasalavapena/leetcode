class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        start = 0
        prev = None
        
        max_size = 1
        
        for i, n in enumerate(nums):
            if prev is not None and prev >= n:
                max_size = max(max_size, i-start)
                start = i
            if i != len(nums)-1:
                prev = n
        if prev and prev < nums[i]:
            return max(max_size, i-start+1)
        return max_size #
            
        