class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [0] * N
        current_min = prices[0]
        for i in range(1, N):
            if prices[i] > current_min:
                dp[i] = prices[i] - current_min
            else:
                current_min = min(prices[i], current_min)
            dp[i] = max(dp[i], dp[i-1]) 

        return dp[-1]