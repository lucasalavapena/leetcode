# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = res = ListNode()
        curr_sum = 0
        head = head.next
        while head:
            if head.val != 0:
                curr_sum += head.val
            else:
                curr.next = ListNode(curr_sum)
                curr = curr.next
                curr_sum = 0
            
            head = head.next
                

        return res.next