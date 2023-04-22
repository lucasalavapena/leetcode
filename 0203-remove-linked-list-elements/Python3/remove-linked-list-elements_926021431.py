# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = dummy
        while curr:
            prev = curr
            curr = prev.next 
            while curr and curr.val == val: 
                prev.next = curr.next
                curr = curr.next
            if curr is None: break
        return dummy.next