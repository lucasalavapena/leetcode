class DSU:
    def __init__(self, N):
        self.p = list(range(N)) 
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        
        self.p[x] = y 
            
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(set(chain(*edges)))
        dsu = DSU(N)
        for (a, b) in edges:
            if dsu.find(a-1) == dsu.find(b-1):
                return [a, b]
            else:
                dsu.union(a-1, b-1)
