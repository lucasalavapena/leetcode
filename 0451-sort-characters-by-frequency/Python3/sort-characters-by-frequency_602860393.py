class Solution:
    def frequencySort(self, s: str) -> str:
        buckets = [[] for i in range(len(s)+1)]
        c = Counter(s)
        for w, count in c.items():buckets[count].append(w)
        flatten = list(chain(*buckets))
        res = [i * c[i] for i in flatten[::-1]]
        return "".join(res)