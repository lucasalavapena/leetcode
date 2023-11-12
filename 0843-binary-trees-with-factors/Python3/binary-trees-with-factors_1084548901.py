from collections import defaultdict

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        factors = defaultdict(int)
        total = 0
        arr.sort()
        set_arr = set(arr)

        for i, n in enumerate(arr):
            factors[n] += 1
            total = (total + 1) % (10**9 + 7)
            early_stopping = float("inf")
            for j in range(i):
                val = arr[j]
                if 2 * val > n or early_stopping <= val:
                    break
                # print(f"{val=}")
                if n % val == 0:
                    factor_required = n / val
                    if factor_required in set_arr:
                        # it is sorted so this should work
                        early_stopping = factor_required
                        if factor_required == val:
                            addition = (factors[val] * factors[factor_required])
                        else:
                            addition = (2 * factors[val] * factors[factor_required])
                        factors[n] = (factors[n] + addition)
                        total = (total + addition) % (10**9 + 7)


        return total