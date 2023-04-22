class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1] * len(nums)
        left_prod[0] = nums[0]
        
        for i, n in enumerate(nums[1:]):
            left_prod[i + 1] = left_prod[i] * n
                    
        right_prod = [1] * len(nums)
        right_prod[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            right_prod[i] = right_prod[i + 1] * nums[i]
        
        res = [1] * len(nums)
                
        for i in range(len(nums)):
            if i == 0:
                res[i] = right_prod[1]
            elif i == len(nums)-1:
                res[i] = left_prod[-2]
            else:
                res[i] = left_prod[i-1] * right_prod[i + 1]
                
        return res
        
        
        