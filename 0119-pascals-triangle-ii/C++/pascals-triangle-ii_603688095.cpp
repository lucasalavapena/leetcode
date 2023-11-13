class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> ans;
        int lhs = 0;
        int rhs = 0;

        ans.push_back({1});
        
        for (int row = 1; row < rowIndex + 1; row++) {
            ans.push_back({});
            for (int j = 0; j < row + 1; j++) {
                lhs = j-1 >= 0 ? ans[row-1][j-1] : 0;
                rhs = j != row ? ans[row-1][j] : 0;
                ans[row].push_back(lhs + rhs);
            }
        }
        
        
        return ans.back();
    }
};
