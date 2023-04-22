# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# def nested_sum(L):
#     return sum( nested_sum(x) if isinstance(x, list) else x for x in L )
    
class Solution:
    def rob(self, root):
        def dfs(node):
            if not node: return [0, 0]
            L = dfs(node.left)
            R = dfs(node.right)
            return [node.val + L[1] + R[1], max(L) + max(R)]
        
        return max(dfs(root))