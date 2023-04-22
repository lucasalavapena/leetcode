#include <string>
#include <iostream>
#include <map>

using namespace std;

class Solution {
    map<char, int> sym2Val = {
            {'I',1},
            {'V',5},
            {'X',10},
            {'L',50},
            {'C',100},
            {'D',500},
            {'M',1000}
        };
public:

    int romanToInt(string s) {

        int totalVal = 0;
        int prevVal = 0;
        for (char subS: s) {
            if (prevVal >= sym2Val[subS]) {
                totalVal += sym2Val[subS];
            }
            else {
               totalVal += sym2Val[subS];
               totalVal -= 2 * prevVal;
 
            }

            prevVal = sym2Val[subS];
        }
        return totalVal;
    }
};