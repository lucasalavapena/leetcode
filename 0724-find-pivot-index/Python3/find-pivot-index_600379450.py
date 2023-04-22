class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums[1:])
            
        for i in range(len(nums)-1):
            if left_sum == right_sum:
                return i
            
            left_sum += nums[i]
            right_sum -= nums[i+1]
        return len(nums)-1 if left_sum == right_sum else -1