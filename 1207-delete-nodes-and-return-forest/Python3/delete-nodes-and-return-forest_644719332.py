# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)
        
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            dfs(node.right)
            
            if node.val in to_delete:                
                if node.left and node.left.val not in to_delete:
                    res.append(node.left)
                if node.right and node.right.val not in to_delete:
                    res.append(node.right)
            
        
            if node.left and node.left.val in to_delete:
                node.left = None
                
            if node.right and node.right.val in to_delete:
                node.right = None
            
        if root is None:
            return None
        
        dfs(root)
        
        if root.val not in to_delete:
            res.append(root)
        
        return res
            
            
            