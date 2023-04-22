from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        info = defaultdict(list)
        
        for s in strs:
            info["".join(sorted(s))].append(s)
        
        return [i for i in info.values()]
