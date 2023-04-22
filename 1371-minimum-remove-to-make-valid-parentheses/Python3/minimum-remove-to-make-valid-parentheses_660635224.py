class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def clean(s, op, cl):
            balance, ans = 0, ""
            for i in s:
                if i == op:
                    balance += 1
                    ans += i
                elif i == cl and balance > 0:
                    balance -= 1
                    ans += i
                elif i not in "()":
                    ans += i              
            return ans
        
        return clean(clean(s, "(", ")")[::-1], ")", "(")[::-1]