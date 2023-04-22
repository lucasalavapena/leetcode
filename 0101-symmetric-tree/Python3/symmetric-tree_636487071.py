# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.are_symmetric = True
        res = self.isSymmetricHelper(root.left, root.right)
        # print(res)
        return self.are_symmetric 
    
    def isSymmetricHelper(self, lhs, rhs) -> bool:
        if lhs is None and rhs is None:
            return True
        if lhs is None and rhs is not None:
            self.are_symmetric = False
            return False
        if lhs is not None and rhs is None:
            self.are_symmetric = False
            return False
        
        if lhs.val != rhs.val:
            self.are_symmetric = False

            return False
        
        a = self.isSymmetricHelper(lhs.right, rhs.left) 
        b = self.isSymmetricHelper(lhs.left, rhs.right) 

        return a and b