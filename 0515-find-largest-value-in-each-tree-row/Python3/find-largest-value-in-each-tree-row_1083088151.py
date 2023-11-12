# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque([root])
        res = []

        while q:
            q_len = len(q)
            curr_max = float("-inf")

            for _ in range(q_len):
                node = q.popleft()
                curr_max = max(curr_max, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(curr_max)

        return res