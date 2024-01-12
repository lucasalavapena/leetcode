from math import ceil
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort()
        upper_bound = sum(cookies[-ceil(len(cookies)/k):])
        res = upper_bound
        def backtrack(childs, j):
            nonlocal res
            if j == len(cookies):
                res = min(res, max(childs))
                return 
            for i in range(k):
                childs[i] += cookies[j]
                if res > childs[i]: 
                    backtrack(childs, j+1)
                childs[i] -= cookies[j]
        backtrack([0] * k, 0)
        return res

