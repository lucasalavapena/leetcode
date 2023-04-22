# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inorder_traversal(root)[k-1]
        
    def inorder_traversal(self, root):
            return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right) if root else []
            

        
        