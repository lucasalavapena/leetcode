# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = [] 
        
        a = self.inorder_single(root1) 
        b = self.inorder_single(root2)
        i, j = 0, 0
        
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
                
        if i == len(a):
            res.extend(b[j:])
            
        elif j == len(b):
            res.extend(a[i:])
        return res
        # return sorted(a)
        # return self.inorder(root1, root2)
    def inorder(self, node1, node2):
        
        if node1 and node2:
            if node1.val < node2.val:
                return self.inorder(node1.left, node2) + [node1.val] + self.inorder(node1.right, node2)
            else:
                return self.inorder(node1, node2.left) + [node2.val] + self.inorder(node1, node2.right)
        elif node1:
            return self.inorder(node1.left, node2) + [node1.val] + self.inorder(node1.right, node2)
        elif node2:
            return self.inorder(node1, node2.left) + [node2.val] + self.inorder(node1, node2.right)
        else:
            return []
        
    
    def inorder_single(self, node):
        return self.inorder_single(node.left) + [node.val] + self.inorder_single(node.right) if node else []