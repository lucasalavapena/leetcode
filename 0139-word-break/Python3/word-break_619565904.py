class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.possible = False
        # check if possible
        
        c = set(s)
        words_cnt = set(chain(*wordDict))
        for i in c:
            if i not in words_cnt:
                return False
        self.wordBreakHelper(s, wordDict, set())
        return self.possible
        
    def wordBreakHelper(self, remaining_s, wordDict, visited):
        if self.possible:
            return
        
        if "" == remaining_s:
            self.possible = True
            return
            
        if remaining_s in visited:
            return
        
        visited.add(remaining_s)
        
        min_length = len(remaining_s)
        
        for word in wordDict:
            if remaining_s.startswith(word):
                n = len(word)
                self.wordBreakHelper(remaining_s[n:], wordDict, visited)
         