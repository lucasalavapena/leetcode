"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        e_d = {i.id: [i.importance, i.subordinates] for i in employees}
        
        total = 0
        q = deque([id])
        
        while q:
            curr_id = q.popleft()
            total += e_d[curr_id][0]
            
            for child in e_d[curr_id][1]:
                q.append(child)
            
            
        return total
        
        
                