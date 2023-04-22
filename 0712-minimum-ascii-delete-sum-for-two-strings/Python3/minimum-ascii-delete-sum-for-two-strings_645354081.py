class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        s1, s2 = [0] + [ord(i) for i in s1], [0] + [ord(i) for i in s2]
        n1, n2 = len(s1), len(s2)
        dp = [[0] * n2 for _ in range(n1)]

        for i1 in range(1,n1): dp[i1][0] = dp[i1-1][0] + s1[i1]
        for i2 in range(1,n2): dp[0][i2] = dp[0][i2-1] + s2[i2]
            
        for i1 in range(1, n1):
            for i2 in range(1, n2):
                if s1[i1] == s2[i2]:
                    dp[i1][i2] = dp[i1-1][i2-1]
                else:
                    dp[i1][i2] = min(dp[i1-1][i2] + s1[i1], dp[i1][i2-1] + s2[i2])
                
        return dp[-1][-1]