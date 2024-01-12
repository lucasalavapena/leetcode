# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node:
                if node.left is None and node.right is None:
                    yield node.val

                yield from dfs(node.left) 
                yield from dfs(node.right)
        
        return all(i == j for i, j in zip_longest(dfs(r1), dfs(r2), fillvalue=201))