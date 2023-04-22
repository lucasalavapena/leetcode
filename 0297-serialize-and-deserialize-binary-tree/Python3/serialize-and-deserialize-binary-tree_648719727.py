# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return "#"
        q = deque([root])
        res = ""
        
        while q:
            q_len = len(q)
            
            for _ in range(q_len):
                node = q.popleft()
                
                if node:
                    res += f"{node.val},"
                else:
                    res += "#,"
                
                if node:
                    q.append(node.left)
                    q.append(node.right)

            res += ";"
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "#": return None
        data_by_level = data.split(";")
        level = 0
        
        root = TreeNode(int(data_by_level[level].split(",")[0]))

        q = deque([root])
        
        
        while q:
            q_len = len(q)
            level += 1
            level_split = data_by_level[level].split(",")
            for i in range(q_len):
                node = q.popleft()
                
                if level_split[2 * i] != "#":
                    left_node = TreeNode(level_split[2 * i])
                    node.left = left_node
                    q.append(left_node)
                    
                
                if level_split[2 * i + 1] != "#":
                    right_node = TreeNode(level_split[2 * i + 1])
                    node.right = right_node
                    q.append(right_node)


        return root
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))