# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.max_diff_helper(root, root.val, root.val)
        
        return self.res
    
    def max_diff_helper(self, node, max_ans, min_ans):
        new_max_ans = max(max_ans, node.val)
        new_min_ans = min(min_ans, node.val)
        
        self.res = max(self.res, new_max_ans- new_min_ans)
        
        L, R = 0, 0
        if node.left:
            L = self.max_diff_helper(node.left, new_max_ans, new_min_ans) 
        if node.right:
            R = self.max_diff_helper(node.right, new_max_ans, new_min_ans)
        
        
#         return max(L, R)
        
        
        
        