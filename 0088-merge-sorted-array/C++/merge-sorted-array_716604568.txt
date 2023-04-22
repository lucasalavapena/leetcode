class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        unsigned k = m + n -1; 
        m--;
        n--;
        
        while (m >= 0 and n >= 0) {
            if (nums1[m] >= nums2[n]) {
               nums1[k--] = nums1[m--];
            }
            else {
               nums1[k--] = nums2[n--];
            }
            // printf("k: %d v: %d\n", k, nums1[k]);
        }
        while (m >= 0) nums1[k--] = nums1[m--];
        while (n >= 0) nums1[k--] = nums2[n--];
    }
};