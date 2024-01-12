class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 1
        for i in range(1, len(arr)):
            prev = prev + 1 if arr[i] > prev + 1 else arr[i]
        return prev
            

        