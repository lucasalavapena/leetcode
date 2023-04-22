# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        if head.next is None: return head
        
        curr = head
        new_head = head.next
        prev = None
        
        while curr and curr.next:
            tmp = curr.next.next 
            swap_buddy = curr.next
            curr.next.next = curr
            curr.next.next.next = tmp
            if prev is not None:
                prev.next = swap_buddy
            prev = curr
            curr = tmp
            
        return new_head