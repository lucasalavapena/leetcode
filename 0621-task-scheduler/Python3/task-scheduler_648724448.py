class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        C = Counter(tasks)
        heap = [[0,-C[c], c] for c in C]
        time = 0
        while heap:
            time = max(time, heap[0][0])
            p,c,char = heapq.heappop(heap)
            p += n + 1
            c += 1
            if c < 0:
                heapq.heappush(heap,[p,c,char])
            time += 1
        return time