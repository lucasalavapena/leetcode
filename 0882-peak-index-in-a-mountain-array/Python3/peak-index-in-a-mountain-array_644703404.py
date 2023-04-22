class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        beg, end = 0, len(arr)-1
        while beg + 1 < end:
            mid = (beg + end)//2
            if arr[mid-1] < arr[mid]:
                beg = mid
            else:
                end = mid -1
        return end if arr[end-1] < arr[end] else beg
            