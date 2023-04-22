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
    bool hasCycle(ListNode *head) {
        unordered_map<ListNode*, int> visited = {{head, 1}};
        
        if (head == NULL)
            return false;
        
        ListNode* curr = head;
                
        while (curr->next != NULL) {
            curr = curr->next;
            if (visited.find(curr->next) != visited.end()) {
                return true;
            } else {
                visited[curr->next] = 1;
            }
            
            
            
        }
        
        return false;
    }
};