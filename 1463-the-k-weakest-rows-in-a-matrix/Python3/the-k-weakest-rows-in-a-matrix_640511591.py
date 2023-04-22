class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n  = len(mat), len(mat[0])
        h = []
        
        for i in range(m):
            soldier_count = m - bisect_left(mat[i][::-1], 1)
            heappush(h, [-soldier_count, -i])
            
            if len(h) > k:
                heappop(h)
        
        res = deque()
        while h:
            _, idx = heappop(h)
            res.appendleft(-idx) 
        return list(res)
