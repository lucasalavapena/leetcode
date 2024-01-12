class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        nums_set = set(nums)
        N = len(nums)
        max_val = nums[0]
        for i in range(1, N):
            if nums[i] == nums[i-1] + 1:
                max_val += nums[i]
            else:
                break
        for i in range(max_val, 52):
            if i not in nums_set:
                return i
        return max_val
        
    