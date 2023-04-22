class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode) 
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        palindromic_pairs = []
        idxs = {word: idx for idx, word in enumerate(words)}

        len_to_words, lens = collections.defaultdict(set), {}
        for w in words:
            n = lens[w] = len(w)
            len_to_words[n].add(w)
        sorted_lens = sorted(len_to_words)

        for word in words:
            peer = word[::-1]                   # whole word -> peer
            if peer != word and peer in idxs:
                palindromic_pairs.append([idxs[word], idxs[peer]])

            n = lens[word]
            for l in sorted_lens:
                if l >= n: break
                prefix, peer = word[:n-l], word[n-l:][::-1]
                """
                0 word: lls prefix: ll peer: s
                0 word: sssll prefix: ss peer: lls

                """
                if prefix == prefix[::-1] and peer in len_to_words[l]:
                    # print(0, word, prefix, peer)
                    palindromic_pairs.append([idxs[peer], idxs[word]])
                peer, suffix = word[:l][::-1], word[l:]
                
                """
                0 word: a prefix: a peer: ""

                """
                if suffix == suffix[::-1] and peer in len_to_words[l]:
                    
                    # print(1, word, suffix, peer)
                    palindromic_pairs.append([idxs[word], idxs[peer]])
        return palindromic_pairs