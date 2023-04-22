class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(int)
        
        for src, dest in roads:
            graph[src] += 1
            graph[dest] += 1
        
        total = 0
        weighting = {}
        
        heap = [(-v, k) for k, v in graph.items()]
        heapq.heapify(heap)
        
        while n and heap:
            total_neighbours, max_node = heapq.heappop(heap)
            weighting[max_node] = n
            graph.pop(max_node)            
            n -= 1
                        
        
        for src, dest in roads:
            total += weighting[src] + weighting[dest]
        return total
        
        
        
        