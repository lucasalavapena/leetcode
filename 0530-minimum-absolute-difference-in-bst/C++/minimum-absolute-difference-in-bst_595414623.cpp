/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int getMinimumDifference(TreeNode* root) {
        vector<int> res;
        int minValue = INT_MAX;
        res = getNodes(root, res);
        
        // printf("%d", res.size());
        
        for (int i = 0; i < res.size(); i++) {
            for (int j = i + 1; j < res.size(); j++) {
                int diff = abs(res[i] - res[j]);
                if (diff <= minValue) {
                    minValue = diff;
                }
            }       
        }
        return minValue;
            
    }
    
    vector<int> getNodes(TreeNode* root, vector<int> res){
        
        if (!root) {
            return res;
        }
        res.push_back(root->val);
        res = getNodes(root->left, res);
        res = getNodes(root->right, res);

        return res;
    }
};