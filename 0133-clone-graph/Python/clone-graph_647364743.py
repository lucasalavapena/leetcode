"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        return self.dfs(node, {})
    
    
    def dfs(self, nd, visited):
        if nd not in visited:
            cl = Node(nd.val)
            visited[nd] = cl
            for n in nd.neighbors:
                cl.neighbors.append(self.dfs(n, visited))
        return visited[nd]
