class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        PRIME = 1_000_000_007
        dp = [[0] * (target) for i in range(n)]
        
        for i in range(min(k, target)):
            dp[0][i] = 1
        
        # O(ntk)
        for j in range(1, n):
            for t in range(j, target):
                for i in range(1, k + 1):
                    if t-i >= 0:
                        dp[j][t] = (dp[j][t] + dp[j-1][t-i]) % PRIME
                    else:
                        break
        
        return dp[-1][-1]