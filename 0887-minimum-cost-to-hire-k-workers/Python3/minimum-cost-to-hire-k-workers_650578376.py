class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # sort to ensure that we pay every worker their minimum expectation
        workers = sorted([[w/q, q] for q, w in zip(quality, wage)])
        max_heap = []
        total_quality = 0
        min_cost = float("inf")
        
        for r, q in workers:
            heappush(max_heap, -q)
            total_quality += q
            
            if len(max_heap) > k:
                total_quality += heappop(max_heap)
            if len(max_heap) == k:
                min_cost = min(min_cost, total_quality * r)
        return min_cost