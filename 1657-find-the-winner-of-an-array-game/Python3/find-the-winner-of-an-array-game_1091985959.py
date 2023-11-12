from itertools import accumulate

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        N = len(arr)
        max_value = max(arr)
        max_index = arr.index(max_value)

        if max_index >= N:
            return max_value

        max_list = list(accumulate(arr, max))[1:]
        for val, group in groupby(max_list):
            # consquective freq
            if len(list(group)) >= k:
                return val
        # should never reach
        return max_value