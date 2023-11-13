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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        
        
        ListNode* res = new ListNode();
        
        if (l1 == NULL and l2 == NULL) {
            return l1;
        }
        if (l1 != NULL and l2 == NULL) {
            return l1;
        }
        if (l1 == NULL and l2 != NULL) {
            return l2;
        }
        
        ListNode* ans = res;
        ListNode* l1Curr = l1;
        ListNode* l2Curr = l2;
        
        
    
        bool started = false;

        
        while (l1Curr != NULL and l2Curr != NULL) {
    
            // printf("l1 curr: %d; l2 curr: %d\n", l1Curr->val, l2Curr->val);
            
            if (l1Curr->val < l2Curr->val) {
                if (started) {
                    res->next = l1Curr;
                    res = res->next;
                } 

                res->val = l1Curr->val;
                l1Curr = l1Curr->next;
            }
            else {
                if (started) {
                    res->next = l2Curr;
                    res = res->next;
                }
                res->val = l2Curr->val;
                l2Curr = l2Curr->next;
            }
            
            
            started = true;            

        }
        
        if (l1Curr == NULL) {
            res->next = l2Curr;
            // printf("l1Curr done");
            return ans;
        }
        else {
            res->next = l1Curr;
            // printf("l2Curr done");
            return ans;
        }
    }

};