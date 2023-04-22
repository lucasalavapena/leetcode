# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.max_diff = 0
        visited = set()
        self.dfs(root, [root.val])
        return self.max_diff
        
    def dfs(self, node, path):
        if node is None:
            return

        min_val = min(path)
        max_val = max(path)
        
        self.max_diff = max(self.max_diff, max_val-min_val)
        if node.left:
            self.dfs(node.left, path + [node.left.val])
    
        if node.right:
            self.dfs(node.right, path + [node.right.val])


        
        