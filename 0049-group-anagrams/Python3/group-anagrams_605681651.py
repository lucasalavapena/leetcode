from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = itertools.groupby(sorted(strs, key=sorted), sorted)
        return [sorted(members) for _, members in groups]
