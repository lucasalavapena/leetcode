# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        q = deque([root])  
        res = []
        
        while q:
            q_size = len(q)
            curr = None
            for i in range(q_size):
                node = q.popleft()
                
                if curr is None:
                    curr = node.val
                    
                if node.right:
                    q.append(node.right)
                
                if node.left:
                    q.append(node.left)
            res.append(curr)
            
                
        return res