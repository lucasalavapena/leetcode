class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        
        N = len(s)
        bucket = [[] for i in range(N + 1)]
        
        for char, count in cnt.items():
            bucket[count].append(char)
        
        res = []
        for i in range(N, -1, -1):
            for char in bucket[i]:
                res.append(char * i)
        return "".join(res)
            