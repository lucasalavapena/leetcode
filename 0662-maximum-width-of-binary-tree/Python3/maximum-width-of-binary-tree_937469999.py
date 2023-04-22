# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque([(root, 1)])
        level = 0
        max_width = 1
        
        while q:
            q_len = len(q)
            # print([(a[0].val, a[1]) for a in q])

            min_q_idx = q[0][1]
            max_width = max(q[-1][1] - min_q_idx + 1, max_width)
            for _ in range(q_len):
                curr_node, idx = q.popleft()
                # print(f"{curr_node.val} {idx=} {level=}")
                if curr_node.left:
                    left_node_idx = 2**level + 2 * (idx-min_q_idx)  + 1
                    q.append((curr_node.left, left_node_idx))

                if curr_node.right:
                    right_node_idx = 2**level + 2 * (idx-min_q_idx )  + 2 
                    q.append((curr_node.right, right_node_idx))

            level += 1

        return max_width
                 