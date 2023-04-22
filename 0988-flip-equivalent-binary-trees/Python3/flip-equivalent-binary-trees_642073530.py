# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None:
            return root2 is None
        if root2 is None:
            return root1 is None
                
        # return self.flipEquiv(root1.left, root2.right) or self.flipEquiv(root1.right, root2.left) if root1.val == root2.val else False
        return (self.flipEquiv(root1.left, root2.left) or self.flipEquiv(root1.left, root2.right)) and (self.flipEquiv(root1.right, root2.left) or self.flipEquiv(root1.right, root2.right) ) if root1.val == root2.val else False
