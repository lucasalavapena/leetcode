class Solution:
    def build_graph(self, words: List[str]) -> dict:
        
        
        def is_possible(s1, s2):
            for i in range(len(s2)):
                if s1 in s2[:i] + s2[i+1:]:
                    return True     
            return False
            
        
        self.graph = defaultdict(set)
        
        buckets = [[] for i in range(17)]
        for w in words:
            buckets[len(w)].append(w)
                
        for w in words:
            if len(w) < 16 and buckets[len(w) + 1] != []:
                for possible in buckets[len(w) + 1]:
                    if is_possible(w, possible):
                        self.graph[w].add(possible)

    
    def longestStrChain(self, words: List[str]) -> int:
        # build graph
        self.build_graph(words)
        
        self.visited = set()
        self.max_len = 1 if words else 0
        for w in sorted(list(self.graph), key=len):            
            if w not in self.visited:
                self.dfs(w, 1)
        
        return self.max_len
    
    def dfs(self, curr, path_len):
        self.max_len = max(self.max_len, path_len)
        
        
        self.visited.add(curr)
        
        for neigh in self.graph[curr]:
            if neigh not in self.visited:
                self.dfs(neigh, path_len + 1)
