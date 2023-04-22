# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        N = len(preorder)
        root = TreeNode(preorder[0])
        stack = [root]
        
        for i in range(1, N):
            curr = preorder[i]
            node = TreeNode(curr)
            
            if curr > stack[-1].val:
                while (stack and curr > stack[-1].val):
                    temp = stack.pop()
                temp.right = node
            else:
                stack[-1].left = node
            stack.append(node)
            
        return root
        