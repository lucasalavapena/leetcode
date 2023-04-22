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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        return preorderTraversalHelper(root, res);
    }
    
    vector<int> preorderTraversalHelper(TreeNode* root, vector<int> res) {
        if (root) {
            res.push_back(root->val);
        }
        else{
            return res;
        }
        
        res = preorderTraversalHelper(root->left, res);
        res = preorderTraversalHelper(root->right, res);

        return res;
    }
};