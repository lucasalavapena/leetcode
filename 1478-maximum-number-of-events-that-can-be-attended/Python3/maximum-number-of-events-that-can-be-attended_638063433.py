class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=1)
        h = []
        res = d = 0
        while events or h:
            if not h: d = events[-1][0]
            while events and events[-1][0] <= d:
                heapq.heappush(h, events.pop()[1])
            heapq.heappop(h)
            res += 1
            d += 1
            while h and h[0] < d:
                heapq.heappop(h)
        return res