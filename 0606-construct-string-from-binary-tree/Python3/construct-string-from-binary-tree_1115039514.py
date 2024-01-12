# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None: return ""
        curr = str(root.val)
        lhs = self.tree2str(root.left)
        rhs = self.tree2str(root.right)
        if lhs or rhs:
            if rhs:
                curr += f"({lhs})({rhs})"
            else:
                curr += f"({lhs})"
        return curr