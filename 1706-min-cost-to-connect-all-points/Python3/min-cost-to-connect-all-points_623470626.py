import heapq

class DSU:
    def __init__(self, N):
        self.p = list(range(N))
        
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        
        if x == y:
            return False
        else:
            self.p[x] = y
            return True
        
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        forest = DSU(n)
        
        def manhattanDist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                edges.append([manhattanDist(points[i], points[j]), i, j])
        
        edges.sort()
        cost = 0
        for d, a, b in edges:
            if forest.union(a, b):
                cost += d
                n -=1
            
            if n == 1:
                break
        return cost
        
        
        
        
        