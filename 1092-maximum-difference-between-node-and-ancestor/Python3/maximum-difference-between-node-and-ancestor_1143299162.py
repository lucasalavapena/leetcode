# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def helper(node, nmax, nmin):
            if not node:
                return 0
            nmax = max(node.val, nmax)
            nmin = min(node.val, nmin)

            if node.left is None and node.right is None:
                return nmax-nmin
            return max(helper(node.left, nmax, nmin), helper(node.right, nmax, nmin))
        return helper(root, root.val, root.val)