class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        h = [[-v, key] for key, v in c.items()]

        heapq.heapify(h)
        res = [0] * k

        i = 0
        while k-i > 0:
            res[i] = heapq.heappop(h)[1]
            i += 1
            
        return res