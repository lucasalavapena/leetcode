class Node:
    def __init__(self, value: int, children: List[int] = None):
        self.value = value
        self.children = children if children else []
        
    
class Graph:
    def __init__(self):
        self.vertices = {}
        self.parents = {}
        
    def generate_from_input(self, trust: List[List[int]]):
        
        
        
        for truster, trustee in trust:
            
            if truster not in self.vertices:
                self.vertices[truster] = Node(truster) 
                
            if trustee not in self.vertices:
                self.vertices[trustee] = Node(trustee)         
            
            self.vertices[truster].children.append(self.vertices[trustee])
            
            if trustee not in self.parents: 
                self.parents[trustee] = []
                
            self.parents[trustee].append(truster)
    
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if n == 1: return 1
        g = Graph()
        g.generate_from_input(trust)
        
        res = -1
        count = 0
        for k, v in g.vertices.items():
            if v.children == [] and len(g.parents.get(k, [])) == n - 1:
                res = v.value
                count = + 1
                
        if count > 1:
            return -1
        
        return res
        