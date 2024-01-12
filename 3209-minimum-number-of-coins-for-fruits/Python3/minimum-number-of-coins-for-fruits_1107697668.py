class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        N = len(prices)

        @cache
        def dp(idx):
            if idx >= N: return 0
            return prices[idx] + min(dp(i) for i in range(idx + 1, 2 * idx + 3))
        return dp(0)