
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        total = 0
        min_max_idx = [(None, None)] * 26
        for i, c in enumerate(s):
            idx = ord(c) - ord("a")
            min_idx, max_idx = min_max_idx[idx]
            if min_idx is None:
                min_max_idx[idx] = (i, i)
            else:
                min_max_idx[idx] = (min_idx, i)
        
        for i, (min_idx, max_idx) in enumerate(min_max_idx):
            if min_idx is not None and min_idx != max_idx:
                seen = set()
                for idx in range(min_idx + 1, max_idx):
                    if s[idx] not in seen:
                        total += 1
                        seen.add(s[idx])
                        if len(seen) == 26:
                            break
        return total