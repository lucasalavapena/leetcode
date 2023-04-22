class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        e = len(s) -1
        for i, item in enumerate(s):
            tmp = s[e-i]
            s[i] = tmp
            s[e-i] = item
            # print(i, e, tmp)
            if ((e+1)//2)-1 == i:
                break
            