class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words: return 0

        def gen_nei_word(word):
            for i in range(len(word)):
                for c in 'qwertyuiopasdfghjklzxcvbnm':
                    if c != word[i]: yield word[:i]+c+word[i+1:]

        begins, ends, d, seen = {beginWord}, {endWord}, 1, {beginWord}
        while begins and ends:
            if len(begins) > len(ends):  # pick the smaller group for next BFS iteration
                begins, ends = ends, begins
            next_begins = set()
            for word in begins:
                for nei_word in gen_nei_word(word):
                    if nei_word in ends:
                        return d+1
                    if nei_word in words and nei_word not in seen:
                        seen.add(nei_word)
                        next_begins.add(nei_word)
            begins, d = next_begins, d+1
        return 0


        
        
