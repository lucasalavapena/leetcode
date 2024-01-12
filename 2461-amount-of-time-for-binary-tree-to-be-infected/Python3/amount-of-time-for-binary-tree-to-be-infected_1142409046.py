# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:    
        
        q = deque([(root, 0)])
        neigh = defaultdict(set)
        while q:
            curr, parent = q.popleft()
            val = curr.val
            if parent:
                neigh[val].add(parent)
                neigh[parent].add(val)
            if curr.left:
                q.append((curr.left, val))
            if curr.right:
                q.append((curr.right, val))

        q = deque([start])
        time = -1
        while q:
            q_len = len(q)
            time += 1
            for _ in range(q_len):
                v = q.popleft()
                for a in neigh[v]:
                    if a in neigh:
                        q.append(a)
                neigh.pop(v)
        return time


