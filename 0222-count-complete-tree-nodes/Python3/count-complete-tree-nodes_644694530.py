# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        def helper(node, counter, level, path):
            if node is None:
                return 0
            
            if node.left is None and node.right is None:    
                return int(path, 2)
            res = 0
            if node.right and height(node.right) == height(node.left):
                res = helper(node.right, counter + 2**level , level + 1, path + "1")
            else:
                if node.left:
                    res = helper(node.left, counter + 2**level , level + 1, path + "0")
            return res

        return helper(root, 0, 0, "1")