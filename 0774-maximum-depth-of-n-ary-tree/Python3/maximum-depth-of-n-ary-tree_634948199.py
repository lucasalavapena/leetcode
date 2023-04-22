"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        return 1 + max(map(self.maxDepth, root.children or [None]))
        
    def bfs(self, root):
        if not root: return 0
        q = deque([root])
        level = 0
        while q:
            q_size = len(q)
            level += 1
            for _ in range(q_size):
                node = q.popleft()
                
                for child in node.children:
                    q.append(child)
        
        return level

            