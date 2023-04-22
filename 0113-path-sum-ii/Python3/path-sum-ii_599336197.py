# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.paths = []
        if root:
            self.dfs(root, targetSum, [root.val])
        
        return self.paths 
        
        
    def dfs(self, root, targetSum, path):
        if root.left is None and root.right is None: 
            if sum(path) == targetSum:
                self.paths.append(path)
            return 
        
        
        if root.left:
            self.dfs(root.left, targetSum, path + [root.left.val])
            
        if root.right:
            self.dfs(root.right, targetSum, path + [root.right.val])
        return 