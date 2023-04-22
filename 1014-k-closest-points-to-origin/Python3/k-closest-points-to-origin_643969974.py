class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        
        def euclidean(x, y):
            return sqrt(x **2 + y **2)
        
        heap = [[euclidean(*p), p] for p in points]
        heapq.heapify(heap)
        
        for i in range(k):
            _, p = heapq.heappop(heap)
            res.append(p)
        return res
        
        