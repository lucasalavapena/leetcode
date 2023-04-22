# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current = root
        stack = []
        total = 0
        
        while True:
            if current is not None:
                stack.append(current)

                current = current.right


            elif(stack):
                current = stack.pop()

                
                total += current.val
                current.val = total

                current = current.left

            else:
                break

        return root if root else None