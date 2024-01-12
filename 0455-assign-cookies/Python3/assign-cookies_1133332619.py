class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0
        C = len(s)
        if not C: return 0
        prev_curr_idx = 0
        for i, min_size in enumerate(g):
            curr_idx = bisect_left(s, min_size, lo=prev_curr_idx)
            # if not first move it forward
            if curr_idx == prev_curr_idx and i:
                curr_idx += 1
            prev_curr_idx = curr_idx
            # no need to add if at end, because no solution found in array
            if curr_idx == C:
                return cnt
            cnt += 1
        return cnt
