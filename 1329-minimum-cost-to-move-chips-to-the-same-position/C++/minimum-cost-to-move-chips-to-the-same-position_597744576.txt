class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        
        // int minCost = INT_MAX;
        unordered_map<bool, int> counter;
        
        
        for (auto p: position) {
            bool parity = p % 2 == 0;
            counter[parity]++;
        }
        
        if (counter[true] > counter[false]) {
            return counter[false];
        }
        else {
            return counter[true] ;
        }
        
        
        // return minCost;
        
    }
};