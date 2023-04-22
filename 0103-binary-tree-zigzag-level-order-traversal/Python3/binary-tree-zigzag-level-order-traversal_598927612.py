# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        q = deque()
        
        q.append(root)
        
        levels = []
        level_count = 0
        sign = 1

        while q:
            q_size = len(q)
            level = []
            for i in range(q_size):
                curr = q.popleft()
                
                level.append(curr.val)
                
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
                
            levels.append(level[::sign])
            sign *= -1
            
        return levels