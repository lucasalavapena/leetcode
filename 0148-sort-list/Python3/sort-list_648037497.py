# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = merged = ListNode()
        while left and right:
            if left.val < right.val:
                merged.next, left = left, left.next
            else:
                merged.next, right = right, right.next
            merged = merged.next
        merged.next = left or right
        return dummy.next
    
        
    def get_mid(self, start):
        slow, fast = start, start
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid
            