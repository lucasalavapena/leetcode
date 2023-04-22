class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.no_components = n
        self.ranks = [0] * n
        
    def union(self, a, b) -> bool:
        x = self.find(a)
        y = self.find(b)
        
        if x == y:
            return False
        else:
            if self.ranks[x] < self.ranks[y]:
                self.p[x] = y
            elif self.ranks[x] == self.ranks[y]:
                self.p[x] = y
                self.ranks[y] += 1
            else:
                self.p[y] = x
            self.no_components -= 1
            return True
        
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
        

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        dsu = DSU(N)
        
        for entry in isConnected:
            all_ones = [i for i, e in enumerate(entry) if e == 1]
            first = all_ones[0]
            for remaining in all_ones[1:]:
                dsu.union(first, remaining)
        return dsu.no_components