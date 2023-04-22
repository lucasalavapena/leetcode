class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        stack = []
        for i in range(1, len(nums)): 
            if nums[i-1] >= nums[i]: stack.append(i)
                
        if not stack: return True 
        if len(stack) > 1: return False
        i = stack[0]
        return (i == 1 or nums[i-2] < nums[i]) or (i+1 == len(nums) or nums[i-1] < nums[i+1])
            