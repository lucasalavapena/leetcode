# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def are_equal(self, node_1, node_2):
        if node_1 is None and node_2 is None:
            return True
        
        if (node_1 is None and node_2 is not None) or (node_1 is not None and node_2 is None):
            return False
        
        current = True if node_1.val == node_2.val else False
            
     
        return current and self.are_equal(node_1.left, node_2.left) and self.are_equal(node_1.right, node_2.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])
        
        while q:
            curr = q.popleft()
            if self.are_equal(curr, subRoot):
                return True
            
            if curr.left:
                q.append(curr.left)
                
            if curr.right:
                q.append(curr.right)
        return False
                
        
        