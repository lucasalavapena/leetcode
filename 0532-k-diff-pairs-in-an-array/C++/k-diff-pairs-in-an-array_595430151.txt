class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        if (nums.size() == 1)
            return 0;
        
        unordered_map<int, int> frequency;
        int count = 0;
        for (auto n: nums)
            frequency[n]++;
        
        
        for (auto [key, value]: frequency) {
            // printf("%d, %d \n", key, value);
            if (k == 0) {
                if (value > 1) count++; 
                continue;
            }
            if (frequency.count(key) > 0 && frequency.count(key + k) > 0) {
                count++;
            }
        }
        
        return count;
        
        
    }
};