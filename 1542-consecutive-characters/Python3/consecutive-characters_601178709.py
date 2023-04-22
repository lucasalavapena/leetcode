class Solution:
    def maxPower(self, s: str) -> int:
        
        prev = ""
        counter = {}
        maximum_repeated = 1
        
        for si in s:
            if si == prev:
                counter[si] = counter.get(si, 1) + 1
                maximum_repeated = max(counter[si], maximum_repeated)
            else:
                counter[si] = 1
            prev = si
        return maximum_repeated