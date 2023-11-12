class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        heapq.heapify(prices)
        first, second = heapq.heappop(prices), heapq.heappop(prices)
        remaining = money - first - second
        return remaining if remaining >= 0 else money