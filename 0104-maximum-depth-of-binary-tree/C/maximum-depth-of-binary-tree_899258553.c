/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root){
    if (!root)
        return 0;
    int lhs = 1 + maxDepth(root->left);
    int rhs = 1 + maxDepth(root->right);
    return lhs > rhs ? lhs : rhs;
}