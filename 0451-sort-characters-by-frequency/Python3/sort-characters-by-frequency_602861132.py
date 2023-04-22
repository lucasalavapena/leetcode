class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        h = [[-v, key] for key, v in c.items()]

        heapq.heapify(h)
        res = ""
        while h:
            top = heapq.heappop(h)
            res += top[1] * -top[0]
            
        return res