# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        a = self.height(root)
        
        return self.d
        
    def height(self, node):
        if node is None:
            return 0
        
        l = self.height(node.left)
        r = self.height(node.right)
        
        self.d = max(self.d, l+r)
        
        return 1 + max(l, r)