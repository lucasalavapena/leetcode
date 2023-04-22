# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.q = deque([])
        
        def dfs(node):
            if not node: return
            if node.left:
                dfs(node.left)
            self.q.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)

    def next(self) -> int:
        return self.q.popleft()

    def hasNext(self) -> bool:
        if self.q:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()