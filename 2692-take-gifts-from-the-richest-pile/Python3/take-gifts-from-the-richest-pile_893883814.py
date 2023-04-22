from heapq import heapify, heappop, heappush
from math import isqrt

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-g for g in gifts] 
        heapify(heap)
        for i in range(k):
            value = heappop(heap)
            heappush(heap, -isqrt(-value))
        return -sum(heap)