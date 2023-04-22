class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, prev = "", '?'
        for i, c in enumerate(s):
            next = s[i + 1] if i + 1 < len(s) else '?'
            prev = c if c != '?' else {'a', 'b', 'c'}.difference({prev, next}).pop()
            res += prev
        return res