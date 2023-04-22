class Solution:
    def insertIntoBST(self, root, val):
        def dfs(root):
            if val < root.val:
                if root.left:
                    dfs(root.left)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    dfs(root.right)
                else:
                    root.right = TreeNode(val)
        
        if not root: return TreeNode(val)
        dfs(root)
        return root