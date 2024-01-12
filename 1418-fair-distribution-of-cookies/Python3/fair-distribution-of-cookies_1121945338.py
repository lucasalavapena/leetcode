from math import ceil
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort()

        upper_bound = sum(cookies[-ceil(len(cookies)/k):])
        def backtrack(childs, j, res):
            if j == len(cookies):
                return min(res, max(childs))

            for i in range(k):
                childs[i] += cookies[j]
                if childs[i] > upper_bound: 
                    childs[i] -= cookies[j]
                    continue
                res = min(backtrack(childs, j+1, res), res)
                childs[i] -= cookies[j]
            return res
        return backtrack([0] * k, 0, float("inf"))

