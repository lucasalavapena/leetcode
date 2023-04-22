class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = [0] + list(accumulate(nums))
        N = len(nums)
        curr_sum = 0
        l, r = 0, 1
        
        min_length = float("inf")
        
        if prefix_sum[-1] < target:
            return 0
        
        while l <= r:
            if prefix_sum[r]-prefix_sum[l] >= target:
                min_length = min(min_length, r-l)
            if prefix_sum[r]-prefix_sum[l] < target and r < len(prefix_sum)-1:
                r += 1
            else:
                l += 1
        
        return min_length
                    
                    
        
        