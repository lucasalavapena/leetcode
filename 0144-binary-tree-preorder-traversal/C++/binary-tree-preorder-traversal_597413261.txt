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
        stack<TreeNode*> s;
        
        TreeNode* current = root;
        
        while (true) {
            if (current) {
                s.push(current);
                res.push_back(current->val);

                current = current->left;
            }
            else if (!s.empty()) {
                current = s.top();
                s.pop();
                
                current = current->right;
            }
            else {
                break;
            }
        }
        
        return res;
    }

};