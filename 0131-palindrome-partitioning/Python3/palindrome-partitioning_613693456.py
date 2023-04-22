class Solution:
    def is_palindrome(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        
    
    def partition(self, s: str) -> List[List[str]]:
        res = [[i for i in s]]
        res_checker = set()
        
        count = 0
        while count < len(res):
            curr = res[count]
            for i in range(len(curr)-1):
                for j in range(i + 2, len(curr)+1):
                    curr_attempt = "".join(curr[i:j])
                    if self.is_palindrome(curr_attempt):
                        intermediate_res = [*curr[:i], curr_attempt, *curr[j:]]
                        if str(intermediate_res) not in res_checker:
                            res.append(intermediate_res)
                            res_checker.add(str(intermediate_res))
            count += 1
            
        return res