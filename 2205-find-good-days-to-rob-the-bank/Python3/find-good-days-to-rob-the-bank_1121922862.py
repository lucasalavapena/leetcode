class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        N = len(security)
        if time == 0: return list(range(N))
        non_increasing = []
        start = -1
        for i in range(N-1):
            if security[i] >= security[i+1]:
                if i + 1 - start > time:
                    non_increasing.append(i + 1)
            else:
                start = i
        non_decreasing = []

        end = N
        for i in range(N-1, 0, -1):
            if security[i] >= security[i-1]:
                if end + 1 - i > time:
                    non_decreasing.append(i-1)
            else:
                end = i
        return list(set(non_increasing) & set(non_decreasing))

