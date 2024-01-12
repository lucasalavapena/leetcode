class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)//3
        piles.sort()
        return sum(piles[i] for i in range(len(piles)-2, n-1,-2))

