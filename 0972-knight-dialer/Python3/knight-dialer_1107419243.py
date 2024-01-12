class Solution:
    def knightDialer(self, n: int) -> int:
        PRIME = 10**9 + 7
        dp = [[1] * 10 for i in range(n)]

        for i in range(1, n):
            # how to get zeros in the ith step
            # either start from 4, 6
            dp[i][0] = (dp[i-1][4] + dp[i-1][6] ) 
            dp[i][1] = (dp[i-1][6] + dp[i-1][8] ) 
            dp[i][2] = (dp[i-1][7] + dp[i-1][9] )
            dp[i][3] = (dp[i-1][4] + dp[i-1][8] ) 
            dp[i][4] = (dp[i-1][0] +  dp[i-1][3] + dp[i-1][9] ) 
            dp[i][5] = 0
            dp[i][6] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][7] ) 
            dp[i][7] = (dp[i-1][2] + dp[i-1][6] ) 
            dp[i][8] = (dp[i-1][1] + dp[i-1][3] ) 
            dp[i][9] = (dp[i-1][2] + dp[i-1][4] ) 
        return sum(dp[-1]) % PRIME