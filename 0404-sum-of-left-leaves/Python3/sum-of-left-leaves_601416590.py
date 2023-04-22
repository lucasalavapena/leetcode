# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.dfs(root)
        return self.total 
    
    def dfs(self, node):
        if node is None:
            return 
        
        if node.left and node.left.left is None and node.left.right is None:
            self.total += node.left.val
            
        self.dfs(node.left)
        self.dfs(node.right)
            
        return
             