# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur, nxt, pre = dummy, dummy, dummy
        cnt = 0
        while cur.next:
            cnt += 1
            cur = cur.next
            
        while cnt >= k:
            cur = new = pre.next # points to head
            nxt = cur.next # points to next of head
            
            """
            1 -> 2 -> 3 - > 4 -> 5 -> 6 -> 7, k = 3
            1 while:
                cur, new = 1, 1
                nxt = 2
                
                1 -> 2 -> 3 - > 4 -> 5 -> 6 -> 7, k = 3
                c, n; nx
                
                for k - 1:
                    next1 = nxt.next
                   1 -> 2 -> 3 - > 4 -> 5 -> 6 -> 7, k = 3
                   c, n; nx; nx1
                    nxt.next = cur
                   1 -> 2 -> 3 - > 4 -> 5 -> 6 -> 7, k = 3
                   c, n; nx; nx1
                    cur = nxt
                    nxt = next1
            
            
            """
            
            
            for _ in range(k-1):
                next1 = nxt.next
                nxt.next = cur
                cur = nxt
                nxt = next1
            
            pre.next = cur
            new.next = nxt
            pre = new
            cnt -= k
            
        return dummy.next