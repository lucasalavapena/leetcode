from collections import defaultdict

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        num_to_idx = {s: idx for idx, s in enumerate(stones)}

        target = stones[-1]
        origin = defaultdict(lambda: defaultdict(int))
        origin[1][0] = 1

        for i, s in enumerate(stones[1:]):
            for src, k in origin[s].items():
                for new_k in [k-1, k, k +1]:
                    val = new_k + s
                    if val > s and val in num_to_idx:
                        origin[val][s] = new_k

                    if val == target:
                        return True

            if s != target:
                del origin[s]
            # print(f"{origin=}")
        return bool(origin[stones[-1]])
