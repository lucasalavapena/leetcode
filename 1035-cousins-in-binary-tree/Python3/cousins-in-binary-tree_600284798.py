# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        q = deque([root])
        
        x_characertistic = None
        y_characertistic = None
        count = 0
        while q:
            q_size = len(q)
            
            for i in range(q_size):
                curr = q.popleft()
                
                if curr.left: 
                    q.append(curr.left)
                    if curr.left.val == x:
                        x_characertistic = (curr.val, count+1)
                    if curr.left.val == y: 
                        y_characertistic = (curr.val, count+1)

                if curr.right: 
                    q.append(curr.right)
                    if curr.right.val == x:
                        x_characertistic = (curr.val, count+1)
                    if curr.right.val == y: 
                        y_characertistic = (curr.val, count+1)
                    
            count += 1
        if x_characertistic is None or y_characertistic is None:
            return False
            
            
        return x_characertistic[0] != y_characertistic[0] and x_characertistic[1] == y_characertistic[1]