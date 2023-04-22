Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.prefix = defaultdict(set)
        self.suffix = defaultdict(set)
        self.index = {}
        for x,w in enumerate(words):
            
            if w not in self.index:
                for i in xrange(len(w)+1):
                    self.prefix[w[:i]].add(w) 
                    self.suffix[w[i:]].add(w)
                    
            self.index[w] = x
    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        index = -1
        for i in self.prefix[prefix] & self.suffix[suffix]:
            index = max(index,self.index[i])
        return index