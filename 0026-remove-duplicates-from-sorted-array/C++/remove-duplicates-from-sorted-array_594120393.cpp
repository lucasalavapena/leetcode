class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
    
    if (nums.empty())
        return 0;
    
    if (nums.size() == 1)
        return 1;
    
    int sum = 1;
    int prev = nums[0];
        
    auto it = nums.begin() + 1;
        
    while (it != nums.end()) {
        if (prev == *it) {
            prev = *it;
            nums.erase(it);
        }
        else {
            sum++;
            prev = *it;
            it++;
        }
    }
    return sum;
    }
};