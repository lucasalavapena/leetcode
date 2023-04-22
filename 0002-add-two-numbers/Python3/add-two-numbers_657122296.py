# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_top = l1
        curr_bottom = l2
        head_pointer = ListNode()
        curr_res = head_pointer
        carry = 0
        
        while curr_top is not None or curr_bottom is not None:
            
            if curr_top is not None and curr_bottom is not None:
                intermediate_res = curr_top.val + curr_bottom.val
            if curr_top is None:
                intermediate_res = curr_bottom.val

            if curr_bottom is None:
                intermediate_res = curr_top.val
            if 10 > intermediate_res + carry:
                curr_res.val = intermediate_res + carry
                carry = 0
            else:
                curr_res.val = (intermediate_res + carry) % 10
                carry = 1
            
            # if curr_top.next is not None and curr_bottom.next is not None:
            if curr_top is not None:
                curr_top = curr_top.next
            if curr_bottom is not None:
                curr_bottom = curr_bottom.next
                
            if curr_top is not None or curr_bottom is not None:
                curr_res.next = ListNode()
                curr_res = curr_res.next
        if carry == 1:
            curr_res.next = ListNode(val=carry)
        return head_pointer
            