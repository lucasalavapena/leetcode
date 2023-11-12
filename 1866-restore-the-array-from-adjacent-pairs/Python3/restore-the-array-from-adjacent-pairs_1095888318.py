from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        N = len(adjacentPairs)
        num_to_idx = defaultdict(set)

        for i, (u, v) in enumerate(adjacentPairs):
            num_to_idx[u].add(i)
            num_to_idx[v].add(i)

        _, curr_value = min((len(v), n) for n, v in num_to_idx.items())
        res = [curr_value]

        for i in range(N):
            prev_val = res[-1]
            idx = num_to_idx[prev_val].pop()
            neighbour = adjacentPairs[idx][1] if adjacentPairs[idx][0] == prev_val else adjacentPairs[idx][0]
            num_to_idx[neighbour].remove(idx)
            res.append(neighbour)

        return res

