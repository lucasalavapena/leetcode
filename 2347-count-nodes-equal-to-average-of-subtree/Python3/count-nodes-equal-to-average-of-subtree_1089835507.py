# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        total = 0

        def dfs(node, running_total):
            nonlocal total
            if node.left is None and node.right is None:
                total += 1
                return node.val, 1

            lhs, lhs_count = dfs(node.left, running_total) if node.left else (0, 0)
            rhs, rhs_count = dfs(node.right, running_total) if node.right else (0, 0)

            local_count = lhs_count + rhs_count + 1
            running_total = lhs + rhs + node.val
            mean = running_total // local_count

            if mean == node.val:
                total += 1


            return running_total, local_count

        dfs(root, 0)
        return total 
        
