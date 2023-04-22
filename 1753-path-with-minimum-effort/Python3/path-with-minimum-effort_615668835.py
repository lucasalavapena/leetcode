import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        no_rows = len(heights)
        no_cols = len(heights[0])
        # init graph
        def graph_helper(i, j):
            neigh = []
            for m in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                new_i, new_j = i + m[0], j + m[1]
                if 0 <= new_i <  no_rows and 0 <= new_j < no_cols:
                    neigh.append(((new_i, new_j), abs(heights[new_i][new_j] - heights[i][j])))
            return neigh
                        
        dist = [float('inf') for _ in range(no_rows * no_cols)]
        # using row major
        dist[0] = 0
        h = [(0, (0, 0))]
        end = (no_rows-1, no_cols-1)
        end_idx = end[0] * no_cols + end[1]
                
        while h:
            d, u = heappop(h)
            
            if end == u:
                return dist[end_idx] 
            
            dist_idx = u[0] * no_cols + u[1]
            if d == dist[dist_idx]:
                for (neigh, neigh_dist) in graph_helper(u[0], u[1]):
                    dist_idx_v = neigh[0] * no_cols + neigh[1]
                    if max(dist[dist_idx], neigh_dist) < dist[dist_idx_v]:
                        dist[dist_idx_v] = max(dist[dist_idx], neigh_dist)
                        heappush(h, (dist[dist_idx_v], neigh))

        return dist[end_idx]