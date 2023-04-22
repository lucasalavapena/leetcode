class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left_sum = 0 #sum(nums[:-2]) 
        right_sum = sum(nums[1:]) 
        end_idx = len(nums)-1
        
        for i in range(0, end_idx):
            
            if left_sum == right_sum:
                return i
        
            left_sum += nums[i]
            right_sum -= nums[i+1]
        if left_sum == right_sum:
            return end_idx
        return -1
        
        