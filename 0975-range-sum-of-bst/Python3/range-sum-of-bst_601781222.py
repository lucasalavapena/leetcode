# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low = low
        self.high = high
        return self.rangeSumBSTHelper(root)

        
    def rangeSumBSTHelper(self, node):
        if node is None:
            return 0
        
        if self.low > node.val:
            return self.rangeSumBSTHelper(node.right)
            
        if node.val > self.high:
            return self.rangeSumBSTHelper(node.left)
            
        return self.rangeSumBSTHelper(node.left) + node.val + self.rangeSumBSTHelper(node.right) 
