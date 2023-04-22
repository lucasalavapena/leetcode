class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        bool carry = true;
        int n = digits.size() - 1;
        if (digits[n] == 9) {
            // digits.back()++;
            digits[n] = 0;
            // printf("%d \n", digits.size() - 2);
            for (int i = digits.size() - 2; i >= -1; i--) {
                if (i == -1 and carry) {
                    digits.insert(digits.begin(), 1);
                    return digits;
                }
                // printf("%d \n", digits[i]);
                if (carry) {
                    digits[i] += 1;
                    // printf("%d \n", digits[i]);
                    if (digits[i] == 10) {
                        digits[i] = 0;
                        carry = true;
                    }
                    else {
                        carry = false;
                    }
                    
                }
            }
        }
        else {
            digits[n]++;
        }
        return digits;
    }
};