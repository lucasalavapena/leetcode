class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        
      if (hand.size() % groupSize != 0)
            return false;
        
        map<int,int> m;
        for (auto &card : hand)
            m[card]++;
        
        while (m.size()!= 0) {
            int cur = m.begin()->first;
            printf("%d \n", cur);
            for (int i = 0; i < groupSize; i++) {
                if (m[cur+i] == 0)
                    return false;   
                else if (--m[cur+i] < 1)
                    m.erase(cur+i);
            }
        }
        
        return true;
    }
};