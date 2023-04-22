# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, path):
            if node is None:
                return 0
            
            if node.left is None and node.right is None:
                return int("".join(path + [str(node.val)]))
            
            left = dfs(node.left, path + [str(node.val)])
            right = dfs(node.right, path + [str(node.val)])
            return left + right
    
        return dfs(root, [])