class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        N = len(security)
        if time == 0: return list(range(N))
        non_increasing = set()
        start = 0
        for i in range(N-1):
            if security[i] >= security[i+1]:
                if i + 1 - start >= time:
                    non_increasing.add(i + 1)
            else:
                start = i + 1

        non_decreasing = set()
        end = N-1
        for i in range(N-1, 0, -1):
            if security[i] >= security[i-1]:
                if end + 1 - i >= time:
                    non_decreasing.add(i-1)
            else:
                end = i - 1
        print(non_increasing, non_decreasing)
        return list(non_increasing & non_decreasing)

