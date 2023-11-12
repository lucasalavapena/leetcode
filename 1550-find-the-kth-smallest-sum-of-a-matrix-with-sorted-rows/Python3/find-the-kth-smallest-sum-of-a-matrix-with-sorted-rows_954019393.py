class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        
        # sum, idxs used 
        h = [(sum(r[0] for r in mat),) + (0,)*m]
        visited = set()

        for _ in range(k - 1):
            elem = heappop(h)
            # try different rows
            for i in range(m):
                idx_idx = i + 1
                if elem[idx_idx] + 1 >= n: continue
                # modify tuple
                tmp = list(elem)
                # new sum based iif you move
                tmp[0] += (mat[i][elem[idx_idx] + 1] - mat[i][elem[idx_idx]])
                tmp[idx_idx] += 1
                new = tuple(tmp)
                if new not in visited: 
                    heappush(h, new)
                    visited.add(new)
        
        return h[0][0]