class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
        if (nums.empty())
            return 0;
        int count = 0;
        
        int i = 0;
        int j = 1;
        
        while (i < nums.size()) {
            if (nums[i] != val) {
                count++;
                j++;
            }
            else {
                while (j < nums.size()) {
                    if (nums[j] != val) {
                        int tmp = nums[j];
                        nums[i] = tmp;
                        nums[j] = val;
                        j++;
                        count++;
                        break;
                    }
                    j++;
                }
            }
            i++;
        }
        
        return count;
    }
};