# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None: return []
            if node.left is None and node.right is None:
                return [node.val]

            return dfs(node.left) + dfs(node.right)
        
        a = dfs(root1)
        b = dfs(root2)
        if len(a) != len(b): return False
        return all(i == j for i,j in zip(a,b))