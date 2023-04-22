from collections import deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n < 2:
            return 0
        
        graph = defaultdict(set)
        
        for i, n in enumerate(manager):
            graph[n].add(i)
            
        steps = 0
        q = deque([[headID, informTime[headID]]])
        max_cost = 0
        while q:
            idx, cost = q.popleft()
            
            max_cost = max(cost, max_cost)
                        
            for neigh in graph[idx]:
                q.append((neigh, cost + informTime[neigh]))
        return max_cost