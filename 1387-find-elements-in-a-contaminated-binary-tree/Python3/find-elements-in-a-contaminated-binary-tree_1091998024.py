# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.res = []
        # 0 is left 1 is right, True is right
        # nice hack for root
        q = deque([(root, -1, True)])

        while q:
            node, parent_val, side = q.popleft()

            new_val = 2 * parent_val + 2 if side else 2 * parent_val + 1

            self.res.append(new_val) 

            if node.left:
                q.append((node.left, new_val, False))
            if node.right:
                q.append((node.right, new_val, True))

                    
        self.res_as_set = set(self.res)

    def find(self, target: int) -> bool:
        return target in self.res_as_set


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)