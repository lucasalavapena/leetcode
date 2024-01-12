class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if s1[0] != s2[0] or s2[0] != s3[0]:
            return -1

        min_len = min(len(s1), len(s2), len(s3))
        operations = sum([len(s1), len(s2), len(s3)]) - min_len * 3

        for i in range(min_len, 1, -1):
            # print(i, operations)
            if not (s1[:i] == s2[:i] and s2[:i] == s3[:i]):
                operations += 3
            else:
                break
        return operations


