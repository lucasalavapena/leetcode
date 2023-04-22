# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        self.max_path_sum_helper(root)
        return self.res
    
    def max_path_sum_helper(self, node):
        if not node:
            return float("-inf")
        
        if node.left is None and node.right is None:
            return node.val
        
        lhs = self.max_path_sum_helper(node.left)
        rhs = self.max_path_sum_helper(node.right)
        
        max_possible = max(lhs, rhs, lhs + rhs, 0)
        self.res = max(self.res, max_possible + node.val, node.val, lhs, rhs)
        return max(lhs + node.val, rhs + node.val, node.val)