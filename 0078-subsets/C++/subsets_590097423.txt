class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        int total_size = nums.size();
        
        res.push_back({});
        
        for (int i = 0; i < total_size; i++) {
            int a = res.size();
            for (int j = 0; j < a; j++) {
                vector<int> temp = res[j];
                temp.push_back(nums[i]);
                res.push_back(temp);
            }
        }
        return res;
    }
};