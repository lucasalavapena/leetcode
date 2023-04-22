import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        heap = []
        
        for i in range(1, N):
            diff = heights[i] - heights[i-1]
            
            if diff > 0 :
                heapq.heappush(heap, diff)
                
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            
            if bricks < 0:
                return i - 1
        return N - 1
                