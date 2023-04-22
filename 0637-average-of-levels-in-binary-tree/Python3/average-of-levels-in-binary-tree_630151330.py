# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        res = []
        while q:
            q_size = len(q)
            level_sum = 0
            for i in range(q_size):
                node = q.popleft()  
                level_sum += node.val
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                
            res.append(level_sum/q_size)
        return res