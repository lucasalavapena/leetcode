# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_count = 0
        self.dfs(root)
        return self.max_count
        
    def dfs(self, node):
        if not node:
            return 0
        left_len, right_len = self.dfs(node.left), self.dfs(node.right)
        left = (left_len + 1) if node.left and node.left.val == node.val else 0
        right = (right_len + 1) if node.right and node.right.val == node.val else 0
        self.max_count = max(self.max_count, left + right)
        return max(left, right)