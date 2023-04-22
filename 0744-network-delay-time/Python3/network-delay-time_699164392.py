class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:  
        graph = defaultdict(set)
        # create graph
        
        for src, dest, weight in times:
            graph[src].add((dest, weight))
                        
        dist = [float('inf') for j in range(n)]
        dist[k-1] = 0

        h = [(0, k)]
        while h:
            d, loc = heappop(h)
            for (neigh, neigh_dist) in graph[loc]:
                cand = d + neigh_dist
                if cand < dist[neigh-1]:
                    dist[neigh-1] = cand
                    heappush(h, (cand, neigh))
        if max(dist) < float('inf'):
            return max(dist)
        return -1
    
