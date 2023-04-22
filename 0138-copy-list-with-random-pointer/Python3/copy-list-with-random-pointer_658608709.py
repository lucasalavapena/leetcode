"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        reference = {}   
        curr = head

        prev = None 
    
        while curr:
            if curr not in reference:
                reference[curr] = Node(curr.val)
                
            new_node = reference[curr]
            if prev:
                prev.next = new_node
            
            if curr.random in reference:
                new_node.random = reference[curr.random]
            else:
                if curr.random:
                    reference[curr.random] = Node(curr.random.val)
                    new_node.random = reference[curr.random]
            prev = new_node 
            curr = curr.next
            
        return reference[head]