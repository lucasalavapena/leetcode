# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        start_node = None

        def dfs_label(root: Optional[TreeNode]) -> None:
            nonlocal start_node
            if root:
                if root.val == start:
                    start_node = root
                    return
                if root.left and start_node is None:
                    root.left.parent = root
                    dfs_label(root.left)
                if root.right and start_node is None:
                    root.right.parent = root
                    dfs_label(root.right)

        dfs_label(root)
        distances = {}
        q = deque([(0, start_node)])
        max_d = 0
        while q:
            d, node = q.popleft()
            distances[node] = d
            max_d = max(max_d, d)
            if node is not root and hasattr(node, "parent") and node.parent and node.parent not in distances:
                q.append((d + 1, node.parent))
            if node.left and node.left not in distances:
                q.append((d + 1, node.left))
            if node.right and node.right not in distances:
                q.append((d + 1, node.right))

        return max_d

