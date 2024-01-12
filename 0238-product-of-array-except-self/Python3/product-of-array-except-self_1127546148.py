class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        lhs = [0] * (N + 1)
        rhs = [0] * (N + 1)
        lhs[0] = 1
        rhs[-1] = 1

        for i in range(1, N + 1):
            lhs[i] = nums[i-1] * lhs[i-1]
            
        for i in range(N-1, -1, -1):
            rhs[i] = nums[i] * rhs[i+1]
        
        res = [0] * N
        # res[0] = rhs[0]
        # res[-1] = lhs[-1]

        for i in range(1, N + 1):
            res[i-1] = lhs[i-1] * rhs[i]
        return res
