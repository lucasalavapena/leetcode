# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.paths = []
        
        self.dfs(root, f"{root.val}")
        return sum([int(p, 2) for p in self.paths])
        
    def dfs(self, node, path):
        if node.left is None and node.right is None:
            self.paths.append(path)
            return
        
        if node.left:
            self.dfs(node.left, path + str(node.left.val))     
        if node.right:   
            self.dfs(node.right, path + str(node.right.val))