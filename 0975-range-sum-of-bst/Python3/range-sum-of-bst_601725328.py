# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0
        self.low = low
        self.high = high
        self.rangeSumBSTHelper(root)
        return self.total
        
    def rangeSumBSTHelper(self, node):
        if node is None:
            return 0
        
        if self.low <= node.val <= self.high:
            self.total += node.val
        
        self.rangeSumBSTHelper(node.left)
        self.rangeSumBSTHelper(node.right) 
