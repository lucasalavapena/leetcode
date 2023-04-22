class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        front = 0
        back = 1
        longest_substring = min(len(s), 1)
        
        loc = {}
        while front <= len(s) - 1:
            string = s[front: back]
            # print(front, back, string, loc)
            idx = loc.get(string[-1], None)
            # it is repeating
            if idx is not None and front <= idx < back:
                front = idx + 1
            else:    
                # not repeating                 
                longest_substring = max(longest_substring, len(string))
            
            loc[string[-1]] = back - 1
            
            back += 1
        
                
        return longest_substring