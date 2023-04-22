/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    
    
    vector<int> preorder(Node* root) {
        vector<int> ans;
        
        if (!root) return ans;
        
        stack<Node*> s;
        s.push(root);
        
        while (!s.empty()) {
            
            root = s.top();
            ans.push_back(root->val);
            s.pop();
            
            vector<Node*> childrens_reversed = root->children;
            reverse(childrens_reversed.begin(), childrens_reversed.end());
            
            for (Node* child: childrens_reversed) {
                if (child)
                    s.push(child);
            }
            
        }

        return ans;
    }
    
    
};