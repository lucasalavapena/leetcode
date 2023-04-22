# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sortedArrayToBSTHelper(nums, 0, len(nums)-1)
        
        
    def sortedArrayToBSTHelper(self, nums, left, right):
        if left > right:
            return
        
        mid = (left + right)//2
        
        curr = TreeNode(nums[mid])
        curr.left = self.sortedArrayToBSTHelper(nums,left, mid-1)
        curr.right = self.sortedArrayToBSTHelper(nums, mid+1,right)

        return curr
