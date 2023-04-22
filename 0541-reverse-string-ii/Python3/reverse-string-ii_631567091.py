class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(i, j):
            while i < j:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1
        n = len(s)
        s_list = list(s)
        for i in range(0, n, 2 * k):
            reverse(i, min(i + k -1, n-1))
            
        return "".join(s_list)