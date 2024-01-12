from heapq import heappop, heappush
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        preference = sorted(zip(profits, capital), key=lambda x: x[1])
        i = 0
        for _ in range(k):
            # this is the main trick to avoid the heapupush calls
            # classic trick doing this forwards and backwards
            while i < len(preference) and preference[i][1] <= w:
                p, c = preference[i]
                heappush(heap, (-p, c))
                i += 1
            if heap:
                w -= heappop(heap)[0]
        return w
