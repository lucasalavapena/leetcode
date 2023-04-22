class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        N = len(s)
        self.sol = []
        
        def backtracking(curr_path, idx):
            if idx == N:
                if len(curr_path) == 4:
                    self.sol.append(".".join(curr_path))
                return
            if len(curr_path) >= 4:
                return
            
            for i in range(1, min(4, N-idx + 1)):
                if int(s[idx : idx + i]) <= 255:
                    if s[idx] == "0" and i > 1: continue
                    backtracking(curr_path + [s[idx : idx + i]], idx + i)
            
        backtracking([], 0)
            
        return self.sol