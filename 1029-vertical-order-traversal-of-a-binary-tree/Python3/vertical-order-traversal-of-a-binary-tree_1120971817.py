# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def in_order(r, c, node):
            return [(c, r, node.val)] + in_order(r+1, c-1, node.left) + in_order(r+1, c+1, node.right)if node else []
        
        data = sorted(in_order(0, 0, root))
        res = []
        prev=float("inf")

        for i, (c, r, no) in enumerate(data):
            if c == prev:
                cols.append(no)
            else:
                if i != 0: res.append(cols)
                cols = [no]
            prev = c
        if cols:
            res.append(cols)
        return res

