class Solution:
    def destCity(self, p: List[List[str]]) -> str:
        return (set([b for a,b in p])-set([a for a,b in p])).pop()
