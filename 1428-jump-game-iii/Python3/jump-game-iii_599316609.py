
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        adj = {}
        goal = []
        
        for i, a in enumerate(arr):
            if a == 0:
                goal.append(i)

            if i not in adj:
                adj[i] = []
                
            if i + a < len(arr):
                adj[i].append(i + a)
                
            if i - a >= 0:
                adj[i].append(i - a)
        visited = {k: False for k in adj}
        return self.dfs(start, goal, adj, visited)
        
        
        
    def dfs(self, curr, goal, adj, visited):
        goal_reached = False
        
        if curr in goal:
            return True
        
        visited[curr] = True
        
        for child in adj[curr]:
            if not visited[child]:
                goal_reached = self.dfs(child, goal, adj, visited) or goal_reached
        
        
        return goal_reached
