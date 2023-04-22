class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # M x K --> Given M moves and K eggs, what is the maximum floor we can check ?
        M = 300 # big enough number
        dp = [[0 for j in range(K+1)] for i in range(M+1)]
        # Initialization 1 --> no move no floor --> dp[0][*] = 0
        # Initialization 2 --> no egg no floor --> dp[*][0] = 0
        # General case --> we want to find dp[m][k] --> we pick one egg and drop (1 move)
        #              --> now we have k or k-1 eggs, depending on whether the previous egg is broken
        #              --> so in either case, we can at least sum up 1 (first move) + dp[m-1][k] + dp[m-1][k-1] 
        for i in range(1, M+1):
            for j in range(1, K+1):
                dp[i][j] = 1 + dp[i-1][j] + dp[i-1][j-1]
                if dp[i][j] >= N:
                    return i
        return N