# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []

        q = collections.deque([root])
        factor = 1
        while q:
            new_row = []
            q_len = len(q)

            for _ in range(q_len):
                curr_node = q.popleft()
                new_row.append(curr_node.val)

                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)

            res.append(new_row[::(1 * factor)])
            factor *= -1 
        return res