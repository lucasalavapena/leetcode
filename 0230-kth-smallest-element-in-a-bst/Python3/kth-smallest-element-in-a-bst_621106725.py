# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.pinorderTraversal(root)[k -1]
    def pinorderTraversal(self, node):
        return self.pinorderTraversal(node.left) + [node.val] + self.pinorderTraversal(node.right) if node else []