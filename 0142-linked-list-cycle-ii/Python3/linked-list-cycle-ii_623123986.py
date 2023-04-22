# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        fast = slow = head
        
        visited = {head}
        while slow.next:
            slow = slow.next
            if slow not in visited:
                visited.add(slow)
            else:
                return slow
            