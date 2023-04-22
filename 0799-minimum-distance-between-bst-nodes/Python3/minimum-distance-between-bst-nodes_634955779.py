# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        trav = self.inorder(root)
        min_difference = float("inf")
        
        for i in range(1, len(trav)):
            min_difference = min(min_difference, trav[i] - trav[i-1])
        
        return min_difference
    
    def inorder(self, node):
        return self.inorder(node.left) + [node.val] + self.inorder(node.right) if node else [] 