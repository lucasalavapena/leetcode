# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque([[root, 0]])
        max_width = 1
        
        while q:
            q_len = len(q)
            
            min_idx = float("inf")
            max_idx = float("-inf")

            for _ in range(q_len):
                node, idx = q.popleft()
                
                if node.left:
                    q.append([node.left, 2 * idx])
                    
                if node.right:
                    q.append([node.right, 2 * idx + 1])
                    
                min_idx = min(min_idx, idx)
                max_idx = max(max_idx, idx)
                max_width = max(max_width, max_idx - min_idx + 1)
            
        return max_width