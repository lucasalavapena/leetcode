# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.inorderTraversalHelper(root)
        return self.ans
        
    def inorderTraversalHelper(self, node):
        if node is None:
            return
        
        self.inorderTraversalHelper(node.left)
        self.ans.append(node.val)
        self.inorderTraversalHelper(node.right)

        
        
        
        