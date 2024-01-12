from heapq import heapify, heappop, heappush
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = [(-p, c) for p, c in zip(profits, capital)]
        heapify(heap)

        while heap and k > 0:
            curr = []
            while heap and heap[0][1] > w:
                curr.append(heappop(heap))
            if not heap: return w
            w -= heappop(heap)[0]

            # maybe it would be more efficient to use a different ype of heap in which I can do heapify and then merging two heaps is cheaper
            for c in curr:
                heappush(heap, c)

            k -= 1

        return w
