# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_count = 0
        prev = None
        curr_count = 0
        
        res = []
        current = root
        stack = []
        
        while True:
            if current is not None:
                stack.append(current)
                current = current.left 
                
            elif len(stack):
                current = stack.pop()
                
                if prev is None:
                    curr_count = 1
                else:
                    if prev == current.val:
                        curr_count += 1
                    else:
                        curr_count = 1
                        
                if curr_count > max_count:
                    max_count = curr_count
                    res = [current.val]
                elif max_count == curr_count:
                    res.append(current.val)
                # print(res)
                prev = current.val
                
                current = current.right
                
            else: 
                break
        return res