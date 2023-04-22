# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        inorder = self.inorder_traversal(root)
        N = len(inorder)
        head = curr = TreeNode(inorder[0])
        for i in range(1, N):
            curr.right = TreeNode(inorder[i])
            curr = curr.right
        return head
    
    def inorder_traversal(self, node):
        return self.inorder_traversal(node.left) + [node.val] + self.inorder_traversal(node.right) if node else []