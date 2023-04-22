class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for n in nums:
                if n <= i: # discard the negative states
                    dp[i] += dp[i-n]
        return dp[target]