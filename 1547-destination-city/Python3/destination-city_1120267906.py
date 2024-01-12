class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src, dest = set(), set()
        for a,b in paths:
            src.add(a)
            dest.add(b)
        return (dest-src).pop()
