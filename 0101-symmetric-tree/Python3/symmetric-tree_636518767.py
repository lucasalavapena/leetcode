# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricHelper(root.left, root.right)
    
    def isSymmetricHelper(self, lhs, rhs) -> bool:
        if lhs is None and rhs is None:
            return True
        if lhs is None and rhs is not None:
            return False
        if lhs is not None and rhs is None:
            return False
        
        if lhs.val != rhs.val:
            return False
        

        return self.isSymmetricHelper(lhs.right, rhs.left)  and self.isSymmetricHelper(lhs.left, rhs.right)