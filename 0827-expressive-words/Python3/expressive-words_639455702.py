class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def group(s): 
            return [(i, len(list(j))) for i, j in groupby(s)] 

        def check(gr1, gr2):
            if len(gr1) != len(gr2): return False
            for (i1, i2), (j1, j2) in zip(gr1, gr2):
                if i1 != j1: return False
                if i2 < j2 or i2 == 2 and j2 == 1: return False
            return True

        s_group = group(s)
        return sum(check(s_group, group(word)) for word in words)