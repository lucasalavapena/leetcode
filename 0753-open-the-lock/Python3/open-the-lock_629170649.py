from collections import deque

class Solution:
    def combinations(self, x):        
        for i in range(len(x)):
            yield x[:i] + str((int(x[i]) -1) % 10) + x[i + 1:]
            yield x[:i] + str((int(x[i]) +1) % 10) + x[i + 1:]
                       
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        start = "0000"
        
        visited = set()
        visited.add(start)
        q = deque([[start, 0]])
        
        if set(self.combinations(target)).issubset(deadends) or start in deadends:
            return -1
        
        while q:
            curr, move_count = q.popleft()
            
            if curr == target:
                return move_count
            
            for elem in self.combinations(curr):
                if elem not in visited and elem not in deadends:
                    q.append([elem, move_count+1])
                    visited.add(elem)
        return -1