# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: return TreeNode(val=val)

        head = curr = root
        
        self.searchInsert(root, val)
        
        return head
        
    def searchInsert(self, node, val):
        if node is None: return
        
        if node.val > val:
            if node.left:
                self.searchInsert(node.left, val)
            else:
                node.left = TreeNode(val=val)
        else:
            if node.right:
                self.searchInsert(node.right, val)
            else:
                node.right = TreeNode(val=val)
        
        