class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.combinations = []
        self.combinationSumHelper(candidates, target, [])
        return self.res
        
    def combinationSumHelper(self, candidates, target, path):
        if target == 0:
            if (c := Counter(path)) not in self.combinations:
                self.res.append(path)
                self.combinations.append(c)
                return
        if target < 0:
            return
        
        for c in candidates:
            self.combinationSumHelper(candidates, target-c, path + [c])
        
        
                