from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if not edges:
            return True
        adj = [[] for _ in range(n)]
        for v, e in edges:
            adj[v].append(e)
            adj[e].append(v)
            
        return self.bfs(adj, start, end)
    
    def bfs(self, adj, start, end):
        q = deque()
        q.append(start)
        seen = set()
        while q:
            curr = q.pop()
            for child in adj[curr]:
                if child in seen:
                    continue
                seen.add(child)
                if child == end:
                    return True
                for i in adj[child]:
                    q.append(i)
        return False
