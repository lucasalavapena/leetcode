# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.total = 0
        self.helper(root, "None")
        return self.total
    
    def helper(self, node, side):
        if node is None:
            return 
        if node.left is None and node.right is None:
            if side == "L":
                self.total += node.val
            return
        
        self.helper(node.left, "L")
        self.helper(node.right, "R")
