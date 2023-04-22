class Solution:
    def maxCoins(self, A):
        if len(A) > 1 and len(set(A)) == 1:
            return (A[0] ** 3) * (len(A) - 2) + A[0] ** 2 + A[0]
        A = [1] + A + [1]
        
        @cache
        def dp(l, r):
            if l > r:
                return 0
            
            res = 0
            for i in range(l, r + 1):
                coins = A[l-1] * A[i] * A[r + 1]
                coins += dp(l, i - 1) + dp(i + 1, r)
                res = max(res, coins)
            return res
        
        return dp(1, len(A)-2)