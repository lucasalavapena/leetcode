"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return None
        head = root
        q = deque([root])
        
        while q:
            q_size = len(q)
            for i in range(q_size):
                curr = q.popleft()
                nxt = q[0] if q and i < q_size-1 else None
                curr.next = nxt
                
                if curr.left: 
                    q.append(curr.left)

                if curr.right: 
                    q.append(curr.right)

        return head