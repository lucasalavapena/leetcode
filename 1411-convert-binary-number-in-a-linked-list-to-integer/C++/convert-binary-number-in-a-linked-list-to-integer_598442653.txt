/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        vector<int> trav;
        
        ListNode* curr = head;
        
        while (curr) {
            trav.push_back(curr->val);
            curr = curr->next;
        }
        int res = 0;
        int lastIdx = trav.size()-1;
        for (int i = 0;i < trav.size(); i++) {
            res += trav[lastIdx-i] * pow(2, i);
        }
        
        return res;
    }
};