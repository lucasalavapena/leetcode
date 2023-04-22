# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        
        curr = head
        # enter solution in the deque structure
        while curr:
            q.append(curr)
            curr = curr.next
            
        
        curr = q.popleft()
        # create solution
        while q:
            curr.next = q.pop()
            curr = curr.next
            if q:
                curr.next = q.popleft()
                curr = curr.next
        curr.next = None
        return head
        
        