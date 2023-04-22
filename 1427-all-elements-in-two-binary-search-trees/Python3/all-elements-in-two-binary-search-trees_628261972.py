# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # self.res = [] 
        
        a = self.inorder_single(root1) + self.inorder_single(root2)
        return sorted(a)
        
        
    def inorder(self, node1, node2):
        pass
    
    def inorder_single(self, node):
        return self.inorder_single(node.left) + [node.val] + self.inorder_single(node.right) if node else []