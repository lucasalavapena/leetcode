class DSU:
    def __init__(self, n):
        self.pr = list(range(n))
        self.connected_components = n
        
    def find(self, x):
        if self.pr[x] != x:
            self.pr[x] = self.find(self.pr[x])
        return self.pr[x]
        
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        
        if x == y :
            return False
        else:
            self.connected_components -= 1
            self.pr[x] = y
            return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        dsu = DSU(N) 
        
        # all_set = set(list(range(N))
        
        for i, connections in enumerate(graph):
            if connections:
                first_connection = connections[0]
                for conn in connections:
                    if dsu.find(i) == dsu.find(conn): return False
                    dsu.union(first_connection, conn)

        return True
            
        
        
        
        