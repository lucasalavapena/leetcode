class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        self.dfs(0, candidates, target, [])
        return self.res
    def dfs(self, idx, candidates: List[int], target, path):
        if target == 0:
            self.res.append(path)
            return 

        
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                    continue
            if candidates[i] > target:
                break
            self.dfs(i + 1, candidates, target - candidates[i], path + [candidates[i]])
        
        
        
        
