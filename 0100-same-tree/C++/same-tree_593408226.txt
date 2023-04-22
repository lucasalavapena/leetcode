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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == NULL and q == NULL)
            return true;
        if (p != NULL and q == NULL)
            return false;
        if (p == NULL and q != NULL)
            return false;
        
        // printf("p: %d q: %d \n", p->val, q->val);
        if (p->val != q->val)
            return false;
        
        bool state1 = isSameTree(p->left, q->left);        
        bool state2 = isSameTree(p->right, q->right);

        
        return state1 and state2;
    }
};