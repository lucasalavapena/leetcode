class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjs = {}
        
        max_children = 0
        max_element = 0
        for e1, e2 in edges:
            adjs[e1] = adjs.get(e1, 0) + 1
            adjs[e2] = adjs.get(e2, 0) + 1
            
            if adjs.get(e1) > 1:
                return e1
            
            if adjs.get(e2) > 1:
                return e2
