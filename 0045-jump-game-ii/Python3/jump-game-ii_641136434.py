class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [float("inf")] * N
        dp[-1] = 0
        
        for i in range(N-2,-1, -1):
            # N -i
            for j in range(1, min(nums[i] + 1, N - i)):
                dp[i] = min(dp[i], 1 + dp[i + j])
        
        return dp[0]