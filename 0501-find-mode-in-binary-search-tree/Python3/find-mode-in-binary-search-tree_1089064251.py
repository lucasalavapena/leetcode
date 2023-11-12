# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt = defaultdict(int)
        max_freq = 0 
        modes = []
        q = deque([root])

        while q:
            q_len = len(q)
            for i in range(q_len):
                n = q.popleft()
                cnt[n.val] += 1

                if cnt[n.val] > max_freq:
                    max_freq = cnt[n.val]
                    modes = [n.val]
                elif cnt[n.val] == max_freq:
                    modes += [n.val]


                if n.left:
                    q.append(n.left)
                if n.right:               
                    q.append(n.right)
        return modes

            
