class DSU:
    def __init__(self, N):
        self.pr = list(range(N))
        self.connected_components = N
        
    def find(self, x):
        if self.pr[x] != x:
            self.pr[x] = self.find(self.pr[x])
        return self.pr[x]
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        
        if x == y:
            return False
        else:
            self.connected_components -= 1
            self.pr[y] = x
            return True
    
    
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        return self.dsu_approach(stones)
    
    
    def dsu_approach(self, stones):
        N = len(stones)
        
        dsu = DSU(N)
        
        m1 = {} # set for x axis
        m2 = {} # set for y axis
        for i in range(N):
            if stones[i][0] not in m1:
                m1[stones[i][0]] = i
            if stones[i][1] not in m2:
                m2[stones[i][1]] = i

        for i, stone in enumerate(stones):
            if m1[stone[0]] != i:
                dsu.union(i, m1[stone[0]])
            if m2[stone[1]] != i:
                dsu.union(i, m2[stone[1]])
        
        """
        move_count = (n_in_connected_group1 -1) + (n_in_connected_group2 -1) + .. 
        stones- (1 + 1 + 1 )
        stones - components
        """
        return N-dsu.connected_components

        
    
    def dfs_approach(self, stones):
        self.Graph = defaultdict(set)
        
        for x1, y1 in stones:
            for x2, y2 in stones:
                if (y1 != y2 and x1 == x2) or (y1 == y2 and x1 != x2) :
                    self.Graph[(x1, y1)].add((x2, y2))
                    self.Graph[(x2, y2)].add((x1, y1))
        
        best_moves = 0
        for node in self.Graph:
            best_moves = max(self.dfs(node, set(), 0), best_moves)
        return best_moves
    
    def dfs(self, node, visited, count):
            visited.add(node)
        
            max_count = count
        
            for neigh in self.Graph[node]:
                if neigh not in visited:
                    max_count = max(self.dfs(neigh, visited, count + 1), max_count)
    
            return max_count
    
    
    
    
    
    
    
    
    
    