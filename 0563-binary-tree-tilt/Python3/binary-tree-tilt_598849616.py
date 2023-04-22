# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        left_tiltsum, left_sum, right_tiltsum, right_sum = 0, 0, 0, 0 
        if root is None: return 0
        
        if root.left:
            left_tiltsum, left_sum = self.findTiltHelper(root.left)
        if root.right:
            right_tiltsum, right_sum = self.findTiltHelper(root.right)
    
    
    
        return left_tiltsum + right_tiltsum + abs(left_sum - right_sum)
    
    def findTiltHelper(self, curr):
        left_tiltsum, left_sum, right_tiltsum, right_sum = 0, 0, 0, 0 
        if curr.left is None and curr.right is None:
            return 0,  curr.val
        
        if curr.left:
            left_tiltsum, left_sum = self.findTiltHelper(curr.left)
        if curr.right:
            right_tiltsum, right_sum = self.findTiltHelper(curr.right)
        
        return abs(left_sum - right_sum) + left_tiltsum + right_tiltsum, left_sum + right_sum + curr.val
