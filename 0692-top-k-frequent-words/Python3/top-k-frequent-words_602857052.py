class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        buckets = [[] for i in range(len(words))]
        c = Counter(words)

        for w, count in c.items():
            # insertion sort, last element should be the first alphabetically
            if not buckets[count]:
                buckets[count].append(w)
            else:
                has_inserted = False
                for i, item in enumerate(buckets[count]):
                    if item < w:
                        buckets[count].insert(i, w)
                        has_inserted = True
                        break
                if not has_inserted:
                    buckets[count].append(w)
        flatten = list(chain(*buckets))
        return flatten[::-1][:k]