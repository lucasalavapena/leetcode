class Solution:
    def countVowelStrings(self, n: int) -> int:
        """
        dp ends with

        """
        dp = [ [1] * 5 for i in range(n)]

        for i in range(1, n):
            # ends in a
            dp[i][0] = dp[i-1][0]

            # ends in e
            dp[i][1] = dp[i-1][0] + dp[i-1][1]

            # ends in i
            dp[i][2] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]

            # ends in o
            dp[i][3] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3]

            # ends in u
            dp[i][4] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4]


        return sum(dp[-1])