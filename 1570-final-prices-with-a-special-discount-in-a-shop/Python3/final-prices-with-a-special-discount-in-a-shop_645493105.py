class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        N = len(prices)
        res = prices[:]
        stack = []
        
        for i in range(N):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                res[idx] = prices[idx] - prices[i]
            stack.append(i)
                
        return res