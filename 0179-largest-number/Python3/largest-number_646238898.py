class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        if len(set(nums)) == 1 and nums[0] == "0":
            return "0"
        
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        nums = sorted(nums, key=cmp_to_key(compare))
        
        return "".join(nums)