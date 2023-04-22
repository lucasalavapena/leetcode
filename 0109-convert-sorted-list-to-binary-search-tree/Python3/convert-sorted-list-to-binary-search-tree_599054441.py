# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        self.head = head
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        return self.sortedListToBSTHelper(0, count-1)
        
    def sortedListToBSTHelper(self, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        left = self.sortedListToBSTHelper(left, mid-1)
        root = TreeNode(self.head.val)
        self.head = self.head.next
        root.left = left
        root.right = self.sortedListToBSTHelper(mid+1, right)

        return root
        
