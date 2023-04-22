# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.paths = []
        self.dfs(root, f"{root.val}")
        return self.paths
    
    def dfs(self, curr, path: str):
        if curr.left is None and curr.right is None:
            self.paths.append(path)
            return 
        
        if curr.left:
            self.dfs(curr.left, path + f"->{curr.left.val}")
        if curr.right:
            self.dfs(curr.right, path + f"->{curr.right.val}")
        return