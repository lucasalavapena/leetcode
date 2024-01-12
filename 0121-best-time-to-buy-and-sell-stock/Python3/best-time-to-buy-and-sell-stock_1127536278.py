class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(prices[i]-min_price, max_profit)
            
        return max_profit