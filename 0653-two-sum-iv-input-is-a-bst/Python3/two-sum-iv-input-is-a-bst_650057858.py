# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = Counter(self.inorder(root))
        for i in s:
            if k-i in s:
                if i == k - i:
                    if s[i] > 1:
                        return True
                else:
                    return True
        return False
        
    
    def inorder(self, node):
        return self.inorder(node.left) + [node.val] + self.inorder(node.right) if node else []