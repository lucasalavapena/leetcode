class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        keys = sorted(list(cnt))
        N = len(keys)
        dp  = [0] * N
        dp[0] = cnt[keys[0]] * keys[0]
        
        for i in range(1, N ):
            if keys[i] - 1 == keys[i-1]:
                dp[i] = max(dp[i-2] + cnt[keys[i]] * keys[i], dp[i-1])
            else:
                dp[i] = dp[i-1] + cnt[keys[i]] * keys[i]
        return dp[-1]
        
        
        
        
        
        
