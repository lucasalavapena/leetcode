# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(node):
    return inorder(node.left) + [node.val] + inorder(node.right) if node else []

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        return sorted(inorder(root1) + inorder(root2))