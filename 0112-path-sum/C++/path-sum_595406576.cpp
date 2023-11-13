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
    bool hasPathSum(TreeNode* root, int targetSum) {
        
        if (!root)
            return false;
        
        if (root->val == targetSum && (root->left == NULL && root->right == NULL)) {
            return true;
        }
        
        return hasPathSumHelper(root->left, root->val, targetSum) or hasPathSumHelper(root->right, root->val, targetSum);       
    }

    bool hasPathSumHelper(TreeNode* node, int currSum, int targetSum) {

        
        if (!node)
            return false;
        
        
        currSum = node->val + currSum;
        if (currSum == targetSum && node->left == NULL && node->right == NULL) {
            // printf("val: %d\n", node->left);
            return true;
        }
        else {
            return hasPathSumHelper(node->left, currSum, targetSum) or hasPathSumHelper(node->right, currSum, targetSum);

        }
        
        return false;
        
    }

};