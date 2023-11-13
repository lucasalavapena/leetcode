/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        unordered_map<ListNode*, int> hashMap;
        
        ListNode* curr = headA;
        while (curr) {
            hashMap[curr]++;
            curr = curr->next;
        }
        
        curr = headB;
        while (curr) {
            if (hashMap.find(curr) != hashMap.end()) {
                return curr;
            }
            hashMap[curr]++;
            curr = curr->next;
        }
        return NULL;
        
    }
};