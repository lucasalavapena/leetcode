import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        no_rows = len(heights)
        no_cols = len(heights[0])
        # init graph
        graph = defaultdict(set)
        
        for i in range(no_rows):
            for j in range(no_cols):
                for m in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    new_i, new_j = i + m[0], j + m[1]
                    if 0 <= new_i <  no_rows and 0 <= new_j < no_cols:
                        graph[(i, j)].add(((new_i, new_j), abs(heights[new_i][new_j] - heights[i][j])))
                        
        dist = [float('inf') for _ in range(no_rows * no_cols)]
        # using row major
        dist[0] = 0
        h = [((0, 0), 0)]
                
        while h:
            u, d = heappop(h)
            dist_idx = u[0] * no_cols + u[1]
            if d == dist[dist_idx]:
                for (neigh, neigh_dist) in graph[u]:
                    dist_idx_v = neigh[0] * no_cols + neigh[1]
                    if max(dist[dist_idx], neigh_dist) < dist[dist_idx_v]:
                        dist[dist_idx_v] = max(dist[dist_idx], neigh_dist)
                        heappush(h, (neigh, dist[dist_idx_v]))
        end = (no_rows-1, no_cols-1)
        end_idx = end[0] * no_cols + end[1]
        return dist[end_idx]