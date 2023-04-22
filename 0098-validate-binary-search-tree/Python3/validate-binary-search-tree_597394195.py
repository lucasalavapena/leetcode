# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        prev = None

        current = root
        stack = []
        while True:

            # Reach the left most Node of the current Node
            if current is not None:

                # Place pointer to a tree node on the stack
                # before traversing the node's left subtree
                stack.append(current)

                current = current.left


            # BackTrack from the empty subtree and visit the Node
            # at the top of the stack; however, if the stack is
            # empty you are done
            elif(stack):
                current = stack.pop()
                
                if prev is not None and prev >= current.val:
                    return False
                prev = current.val
                
                # We have visited the node and its left
                # subtree. Now, it's right subtree's turn
                current = current.right

            else:
                break

        return True


        