# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        self.good_nodes_helper(root, -100_000)
        return self.res
        
    def good_nodes_helper(self, node: TreeNode, max_from_path):
        if node is None: return
        
        if node.val >= max_from_path:
            self.res += 1
        
        self.good_nodes_helper(node.left, max(max_from_path, node.val))
        self.good_nodes_helper(node.right, max(max_from_path, node.val))