class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> counter;
        int length = nums.size();
        
        for (unsigned i = 0; i <  length; i++) {
            if (counter.find(nums[i]) == counter.end()) {
                counter[nums[i]] = 1 ;
            }
            else {
                counter[nums[i]]++;
            }
                
            if (counter[nums[i]] > length/2) {
                return nums[i];
            }
        }
        return -1;
        
    }
};