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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (!root) return {};
        
        queue<TreeNode*> q;
        vector<vector<int>> res;
        
        TreeNode* curr;
        int len;
        q.push(root);
        while(!q.empty()){
               len = q.size();
		       vector<int> v;
               for(int i=0;i<len;i++){
                    curr = q.front();
                    q.pop();
                    v.push_back(curr->val);

                   if(curr->left) q.push(curr->left);
                   if(curr->right) q.push(curr->right);
                }
		        res.push_back(v);
            }
        
        return res;
    }
};