class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = [0] * len(queries)

        min_start = len(words) - 1
        max_end = 0

        for start, end in queries:
            min_start = min(start, min_start)
            max_end = max(end, max_end)
        
        acc = [0] * (max_end - min_start + 2)
        for i in range(min_start, max_end + 1):
            delta = 0 
            if words[i][0] in vowels and words[i][-1] in vowels:
                delta = 1 
            acc[i - min_start + 1] = acc[i - min_start] + delta

        for i, (start, end) in enumerate(queries):
            res[i] = acc[end - min_start + 1] - acc[start - min_start]

        return res


