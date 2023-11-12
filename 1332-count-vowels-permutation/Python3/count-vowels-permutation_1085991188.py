class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        dp tablet
        n a e i o u total?
        1
        2
        3
        4

        """
        PRIME = 10**9 + 7
        dp = [[0] * 5 for i in range(n)]
        dp[0] = [1, 1, 1, 1, 1]

        for i in range(1, n):

            # a: *e -> *ea, *i -> ia, *u -> *ua
            # 
            dp[i][0] = (dp[i-1][1] +  dp[i-1][2] + dp[i-1][4])  % PRIME

            # e: *a leads to *ae, *i -> ie
            dp[i][1] = (dp[i-1][0] +  dp[i-1][2])  % PRIME


            # i: *e leads to *ei, *o -> *oi
            dp[i][2] = (dp[i-1][1] +  dp[i-1][3])  % PRIME

            # o: *i -> io
            dp[i][3] = dp[i-1][2]

            # u: *i -> iu, *o -> *ou
            dp[i][4] = (dp[i-1][2] +  dp[i-1][3])  % PRIME


        return sum(dp[-1]) % PRIME