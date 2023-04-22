class Node:
    def __init__(self, val_, children=None):
        self.val = val_
        self.children = [] if children is None else children

    def add_children(self, child):
        self.children.append(child)
        
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if n == 1 and start == end: return True
        
        graph_nodes = {}
        
        
        for e1, e2 in edges:
            if e1 not in graph_nodes:
                g = Node(e1)
                graph_nodes[e1] = g
                
            if e2 not in graph_nodes:
                g2 = Node(e2)
                graph_nodes[e2] = g2

            graph_nodes[e1].add_children(graph_nodes[e2])
            graph_nodes[e2].add_children(graph_nodes[e1])
    
        visited = {g: False for g in graph_nodes.values()}
        goal_reached = self.dfs(graph_nodes[start], graph_nodes[end], visited)
    
        return goal_reached
        
    def dfs(self, curr, goal, visited):
        goal_reached = False


        visited[curr] = True
        
        if visited[goal]:
    
            return True
                
        
            
        for g in curr.children:
            if not visited[g]:
                goal_reached = self.dfs(g, goal, visited) or goal_reached
                if goal_reached:
                    return goal_reached
                
        if not goal_reached:
            return goal_reached
    
        return goal_reached