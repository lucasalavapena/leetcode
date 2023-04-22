class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        N = len(s)
        self.res = []
        
        def backtracking(s, i, path):
            if len(path) == 4 and i == N:
                self.res.append(".".join(path))
                return
            if len(path) >= 4 or i >= N:
                return
            
            for j in range(1, 4):
                val = s[i: i + j]
                if j > 1 and  val[0] == "0":
                    continue
                if 0 <= int(val) < 256:
                    backtracking(s, i + j, path + [val])
        
        backtracking(s, 0, [])
        
        return self.res