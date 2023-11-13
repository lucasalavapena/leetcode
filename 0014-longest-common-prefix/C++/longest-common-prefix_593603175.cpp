class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
        string longest_substring = strs[0];
        
        for (unsigned j = 1; j < strs.size(); j++) {
            string s = strs[j]; 
            int substring_size = min(s.size(), longest_substring.size());
            longest_substring.resize(substring_size);
            for (unsigned i = 0; i < substring_size; i++) {
                if (s[i] == longest_substring[i]) {
                    continue;
                } else {
                    longest_substring.resize(i);
                    break;
                }
            }
        }
        return longest_substring;
    }
};