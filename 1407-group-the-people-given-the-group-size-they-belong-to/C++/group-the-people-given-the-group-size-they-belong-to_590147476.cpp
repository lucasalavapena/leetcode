#include <algorithm>    // std::count
#include <vector>       // std::vector

class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        vector<vector<int>> res;
	    unordered_map<int,vector<int>> groups;
                
        
        for(int i=0; i < groupSizes.size(); i++){
            groups[groupSizes[i]].push_back(i);
            if (groups[groupSizes[i]].size() == groupSizes[i]) { 
                res.push_back(groups[groupSizes[i]]); 
                groups[groupSizes[i]]={};
            }
        }

        return res;
    }
};