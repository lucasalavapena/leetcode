# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        a = set(self.inorder(root))
        for b in a:
            if k-b in a and k-b != b:
                return True
        return False
    
    def inorder(self, node):
        return [node.val] + self.inorder(node.left) + self.inorder(node.right) if node else []