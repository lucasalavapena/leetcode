class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxValue = nums[0];
        int currSum = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            currSum = max(nums[i], nums[i] + currSum);
            maxValue = max(currSum, maxValue);
        }
        
        return maxValue;
    }

    
};