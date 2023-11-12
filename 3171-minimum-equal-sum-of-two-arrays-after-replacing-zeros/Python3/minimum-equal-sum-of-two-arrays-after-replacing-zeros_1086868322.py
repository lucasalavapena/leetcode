class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_sum = sum(nums1)
        nums1_zero_cnt = nums1.count(0)
        nums2_sum = sum(nums2)
        nums2_zero_cnt = nums2.count(0)

        if nums1_zero_cnt == 0:
            if nums2_sum + nums2_zero_cnt > nums1_sum:
                return -1
            return nums1_sum if nums2_zero_cnt != 0 else (nums2_sum if nums2_sum == nums1_sum else -1)


        if nums2_zero_cnt == 0:
            if nums1_sum + nums1_zero_cnt > nums2_sum:
                return -1
            return nums2_sum 

        return max((nums1_sum + nums1_zero_cnt), (nums2_sum + nums2_zero_cnt) )