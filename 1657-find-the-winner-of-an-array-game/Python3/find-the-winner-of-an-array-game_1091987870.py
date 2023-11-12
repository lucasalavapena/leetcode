from itertools import accumulate

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        N = len(arr)
        max_value = max(arr)
        max_index = arr.index(max_value)

        if max_index >= N:
            return max_value

        max_list = accumulate(arr, max)
        next(max_list)
        prev_count = 0
        prev = None
        for val in max_list:
            if prev == val:
                prev_count += 1
                if prev_count == k:
                    return val
                continue
            
            prev = val
            prev_count = 1


        return max_value