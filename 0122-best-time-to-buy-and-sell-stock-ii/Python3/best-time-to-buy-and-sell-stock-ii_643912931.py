class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        diff = [0] * (N - 1)

        for i in range(1, N):
            diff[i-1] = prices[i] - prices[i-1]
            
        profit = 0       
        for i, d in enumerate(diff):
            if d > 0:
                profit += d
                
        return profit
                    
            