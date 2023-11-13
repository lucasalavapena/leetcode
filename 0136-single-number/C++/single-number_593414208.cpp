class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        int ans = 0;
        
        for(int i=0; i<nums.size(); i++) {
            // printf("nums[i]: %d ans: %d\n", nums[i], ans);
            ans = ans^nums[i];
            // printf("ans: %d\n", ans);
        }
        
        return ans;
    }
};