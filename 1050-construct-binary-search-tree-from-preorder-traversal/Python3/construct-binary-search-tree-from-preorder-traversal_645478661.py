# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        node_val = preorder[0]
        
        node = TreeNode(preorder[0])
        
        i = 1
        while i < len(preorder) and preorder[i] < node.val:
            i += 1

        node.left = self.bstFromPreorder(preorder[1:i])
        node.right = self.bstFromPreorder(preorder[i:])
        
        return node