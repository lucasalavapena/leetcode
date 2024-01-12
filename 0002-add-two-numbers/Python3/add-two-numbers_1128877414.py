# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = l1.val
        l1 = l1.next
        cnt = 1
        while l1:
            a += l1.val * 10**cnt
            l1 = l1.next
            cnt += 1
            
        b = l2.val
        l2 = l2.next
        cnt = 1
        while l2:
            b += l2.val * 10**cnt
            l2 = l2.next
            cnt += 1

        res = a + b
        res_str = str(res)
        head = ListNode(val=int(res_str[-1]))
        curr = head
        for i in range(1, len(res_str)):
            curr.next = ListNode(val=int(res_str[~i]))
            curr = curr.next
        return head
                        
        