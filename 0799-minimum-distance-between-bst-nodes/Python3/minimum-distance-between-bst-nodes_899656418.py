# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder_trav(root):
            return inorder_trav(root.left) + [root.val] + inorder_trav(root.right)  if root else []
        inorder = inorder_trav(root)
        diff = [t - s for s, t in zip(inorder, inorder[1:])]
        return min(diff)