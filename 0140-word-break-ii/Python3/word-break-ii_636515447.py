class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.res = []
        # check if possible
        
        c = set(s)
        words_cnt = set(chain(*wordDict))
        for i in c:
            if i not in words_cnt:
                return []
        self.wordBreakHelper(s, None, wordDict)
        return self.res
        
    def wordBreakHelper(self, remaining_s, path, wordDict):        
        if "" == remaining_s:
            self.res.append(path)
            return
        
        # visited.add(remaining_s)
        
        min_length = len(remaining_s)
        
        for word in wordDict:
            if remaining_s.startswith(word):
                n = len(word)
                self.wordBreakHelper(remaining_s[n:], f"{path} {word}" if path else word, wordDict)
         