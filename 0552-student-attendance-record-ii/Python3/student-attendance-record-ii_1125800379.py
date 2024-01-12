class Solution:
    def checkRecord(self, n: int) -> int:
        PRIME = 1_000_000_007
        # n x 2 x 3
        # 
        dp = [[[0] * 3 for j in range(2)] for i in range(n)]
        # init
        # P
        dp[0][0][0] = 1
        # A
        dp[0][1][0] = 1
        # L
        dp[0][0][1] = 1

        for i in range(1, n):
            for k in range(2):
                for m in range(3):
                    # getting a P, just add evyerthingt from previous
                    dp[i][k][0] = (dp[i][k][0] + dp[i-1][k][m]) % PRIME
                    # getting an L
                    if m < 2:
                        dp[i][k][m + 1] = (dp[i][k][m+1] + dp[i-1][k][m]) % PRIME
            
            # getting an A
            # Note I iniital forgot that you can go to [j==1] from another j==1 state
            dp[i][1][0] = (dp[i-1][1][0] + dp[i-1][1][1] + dp[i-1][1][2] + dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]) % PRIME

        total = 0
        for i in range(2):
            for j in range(3):
                total = (total + dp[-1][i][j]) % PRIME
        return total