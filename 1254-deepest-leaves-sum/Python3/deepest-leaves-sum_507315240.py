# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.q = queue.Queue()
        leaves = []
        
        self.q.put([root, 0])
        
        max_depth = 0
        
        while not self.q.empty():
            curr_node, depth = self.q.get()
            
            if max_depth < depth:
                max_depth = depth
                
            if curr_node.left is None and curr_node.right is None:
                    leaves.append([curr_node, depth]) 
            else:   
                if curr_node.left is not None:
                    self.q.put([curr_node.left, depth + 1])
                if curr_node.right is not None: 
                    self.q.put([curr_node.right, depth + 1])
                    
        leaves_sum = 0
        for l in leaves:
            if l[1] == max_depth:
                leaves_sum += l[0].val

        return leaves_sum

