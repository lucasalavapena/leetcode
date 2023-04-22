class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        res = list(s)        
        for source, idx, target in zip(sources, indices, targets):     
            if s[idx: idx + len(source)] == source:
                res[idx] = target      
                # print(res)
                for i in range(idx + 1, idx + len(source)):
                    res[i] = ""                     
                # print(res)
        return "".join(res)
