class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        N = len(s)
        dp = [0] * N
        dp[0] = 1
        for i in range(1, N):
            if s[i-1] == "1":
                if s[i] == "0":
                    dp[i] =  dp[i-2] if i > 1 else dp[i-1]
                else:
                    dp[i] =  dp[i-1] + (dp[i-2] if i > 1 else 1)
            elif s[i-1] == "2":
                if s[i] > "6": 
                    dp[i] =  dp[i-1] 
                elif s[i] == "0":
                    dp[i] =  dp[i-2] if i > 1 else dp[i-1]
                else:
                    dp[i] =  dp[i-1] + (dp[i-2] if i > 1 else 1)
            else:
                if s[i] == "0": return 0
                dp[i] = dp[i-1]
        return dp[-1]