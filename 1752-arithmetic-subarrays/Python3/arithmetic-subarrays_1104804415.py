class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = [False] * len(l)
        for i, (start_idx, end_idx) in enumerate(zip(l, r)):
            arr = sorted(nums[start_idx:end_idx+1])
            d = arr[1] - arr[0]
            for j in range(2, len(arr)):
                if arr[j] - arr[j-1] != d:
                    break
            else:
                res[i] = True
        return res

