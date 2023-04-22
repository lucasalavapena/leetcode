from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """

        """
        window = Counter()
        desired = Counter(s1)
        desired_len = len(s1)

        for i, s in enumerate(s2):
            window[s] += 1
            if desired_len <= i + 1:
                if desired_len <= i:
                    window[s2[i - desired_len]] -= 1
                if window == desired:
                    return True                          

        return False

