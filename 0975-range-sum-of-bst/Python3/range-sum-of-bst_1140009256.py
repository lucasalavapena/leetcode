# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def get(node):
            return [node.val] + get(node.left) + get(node.right) if node else []
        return sum(c for c in get(root) if low <= c <= high)
        