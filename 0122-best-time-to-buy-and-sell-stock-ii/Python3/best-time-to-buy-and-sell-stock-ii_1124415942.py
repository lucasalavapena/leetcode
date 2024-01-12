class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diffs = [y - x for x, y in zip(prices, prices[1:])]
        return sum(max(0, d) for d in diffs)