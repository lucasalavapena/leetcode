class Solution:
    def searchInsert(self, nums, target):
        return self.tail_recursive_searchInsert(0, nums, target)


    def tail_recursive_searchInsert(self, start, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

          return the position to insert a new element into the sorted list.
          Note: the solution can be implemented in a recursive way.
        """
        size = len(nums)
        if (size == 0):
            # empty input list, early exit
            return start

        mid_index = int(size/2)
        if (nums[mid_index] == target):
            return start + mid_index 
        elif (nums[mid_index] > target):
            return self.tail_recursive_searchInsert(
                            start, nums[0:mid_index], target)
        else:
            return self.tail_recursive_searchInsert(
                            start+mid_index+1, nums[mid_index+1:], target)