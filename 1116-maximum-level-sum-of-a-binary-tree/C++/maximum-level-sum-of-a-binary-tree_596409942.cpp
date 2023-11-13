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
    int maxLevelSum(TreeNode* root) {
        
        if (!root) return 0;
        
        queue<TreeNode*> q;
        q.push(root);
        
        
        TreeNode* tmp;
        int maxSum = INT_MIN;
        int currSum;
        int level = 0;
        int maxLevel = 0;
        while (!q.empty()) {
            int qSize = q.size();
            currSum = 0;
            level++;
            for (int i = 0; i < qSize; i++) {
                tmp = q.front();
                q.pop();
                
                currSum += tmp->val;
                
                if (tmp->left) q.push(tmp->left);
                if (tmp->right) q.push(tmp->right);
                    
            }
            if (currSum > maxSum) {
                maxSum = currSum;
                maxLevel = level;
            }
        }
        return maxLevel;
    }
};