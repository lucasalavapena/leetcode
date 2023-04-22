class Solution {
public:
    int maxProduct(vector<int>& nums) {
        priority_queue<int> pq;
        // priority_queue<int> pq2;

        for (int v: nums) {
            pq.push(v);
            // pq2.push(-v); 
        }


        int a = pq.top();
        pq.pop();
        int b = pq.top();
        
        // int c = -pq2.top();
        // pq2.pop();
        // int d = -pq2.top();
        
        return (a-1) * (b-1);//max(, (c-1) * (d-1));
        
    }
};