# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def dfs(left, right):
            if left > right: return [None]
            if left == right: return [TreeNode(left)]
            res = []
            for i in range(left, right + 1):
                left_nodes = dfs(left, i - 1)
                right_nodes = dfs(i + 1, right)
                for left_node in left_nodes:
                        for right_node in right_nodes:
                            root_node = TreeNode(i, left_node, right_node)
                            res.append(root_node)
            return res
        
        return dfs(1, n)
    