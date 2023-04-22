class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = 10_000, 0
        for p in prices:
            min_price = min(p, min_price)
            max_profit = max(p-min_price, max_profit)
        return max_profit