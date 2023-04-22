class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        m, n = len(wordList[0]), len(wordList)
        words_inverse = {w:i for i, w in enumerate(wordList)}
        
        words_graph = defaultdict(set)

        if endWord not in words_inverse: return 0
        end_ind = words_inverse[endWord]

        # building graph is nm * m (slices) * 26 (alphabet)
        for word in wordList:
            for l in range(m):
                p1, p2 = word[0:l], word[l+1:]
                for i in string.ascii_lowercase:
                    tmp = p1 + i + p2
                    if tmp in words_inverse and tmp != word:
                        words_graph[words_inverse[word]].add(words_inverse[tmp])

        depths = [-1] * (n-1) + [0]
        queue = deque([n-1])

        while queue:
            curr = queue.popleft()
            if curr == end_ind:
                return depths[end_ind]  + 1
            for neib in words_graph[curr]:
                if depths[neib] == -1:
                    queue.append(neib)
                    depths[neib] = depths[curr] + 1
                    
        return 0

        
        
