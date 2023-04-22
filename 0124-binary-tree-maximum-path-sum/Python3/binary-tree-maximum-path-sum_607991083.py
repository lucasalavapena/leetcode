# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf")
        self.dfs(root)
        return self.maxSum
        
    def dfs(self, node):
        if not node:
            return 0
        
        lhs = self.dfs(node.left)
        rhs = self.dfs(node.right)
        
        left = max(lhs + node.left.val, 0) if node.left else lhs
        right = max(rhs + node.right.val, 0) if node.right else rhs
        # self.maxSum = max(self.maxSum, left + node.val + right, node.val, node.val + left, node.val + right)
        self.maxSum = max(self.maxSum, left + node.val + right)

        return max(left, right)