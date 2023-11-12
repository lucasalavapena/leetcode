class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def valid(value):
            a_0 = max(value-index, 1)
            # linear rise to value + 1s if needed
            n_left_linear = value - a_0 + 1
            left_all_ones = max(index + 1 - n_left_linear, 0)
            left_inclusive_sum = n_left_linear/2 * (a_0 + value) + left_all_ones

            # c = sum(max(value - i, 1) for i in range(index + 1))

            remaining = n - index - 1
            # b = sum(max(value -1 - i, 1) for i in range(remaining))

            a_last = max(value-remaining, 1)
            n_right_linear = value - a_last
            right_all_ones = max(remaining - n_right_linear, 0)

            right_sum = n_right_linear/2 * (value - 1 + a_last) + right_all_ones
            # print(f"{index=} {value=}")
            # print(c, left_inclusive_sum)
            # print(b, right_sum)

            return (left_inclusive_sum + right_sum) <= maxSum

        low, high = 1, maxSum

        while low <= high:
            mid = (low + high) // 2
            # print(mid, low, high)
            if valid(mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return high
        