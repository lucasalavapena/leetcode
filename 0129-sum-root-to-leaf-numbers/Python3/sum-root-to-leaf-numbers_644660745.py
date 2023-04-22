# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root, n):
            if not root: return 0
            cur = n * 10 + root.val
            if not root.left and not root.right:
                return cur
            return helper(root.left, cur) + helper(root.right, cur)
        
        return helper(root, 0)