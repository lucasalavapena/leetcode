class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        def is_done(arr: List[int]) -> bool:
            if arr[0] != 1:
                return False

            for i in range(1, len(arr)):
                if abs(arr[i] - arr[i-1]) > 1:
                    return False
            return True

        if is_done(arr):
            return max(arr)

        arr.sort()

        arr[0] = 1


        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) > 1:
                arr[i] = arr[i-1] + 1 if arr[i] > arr[i-1] else arr[i]

        return arr[-1]
            

        