class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        # LCS
        # O(len(dictionary) lg len(dictionary))
        dictionary_sorted = sorted(dictionary, key=len, reverse=True)
        m = len(s)
        
        candidates = []
        candidate_length = -1
        
        for candidate in dictionary_sorted:
            n = len(candidate)
            if n < candidate_length:
                return sorted(candidates)[0]
            
            i, j = 0, 0
            while i < m and j < n:
                if s[i] == candidate[j]:
                    j += 1
                i += 1                    
            
            if j == n:
                candidate_length = n
                candidates.append(candidate)
                
        if candidate_length > 0:
            return sorted(candidates)[0]
        return ""