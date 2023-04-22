/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *   public:
 *     int guess(string word);
 * };
 */
class Solution {
public:
    
    int wordMatches(string str1, string str2) {
        int count = 0;
        for (unsigned i = 0; i < str1.size(); i++) {
            if (str1[i] == str2[i])
                count++;
        }
        return count;
    }
    
    vector<string> findWordWithSameMatch(vector<string>& wordlist, string word, int matchCount) {
        vector<string> res;
        for (auto w : wordlist) {
            if (wordMatches(w, word) == matchCount) {
                res.push_back(w);
            }
        }
        return res;
        
        
    }
    
    void findSecretWord(vector<string>& wordlist, Master& master) {
        // most unique
        
        int guessMatch = -1;
        
        vector<string> currList= wordlist;
        
        string guessString = currList.back();
        int prevSize = currList.size();
        // wordlist.pop_back()
        for (int i = 0; i < 10;i++) {
            remove(currList.begin(),currList.end(),guessString);
                
            guessMatch = master.guess(guessString);
            
            // printf("guess: %d\n", guessMatch);
            if (guessMatch == 6)
                // printf("guess: %d\n", guessMatch);
                break;
            
            
            
            currList = findWordWithSameMatch(currList, guessString, guessMatch);
            
            if (guessMatch == 0 && currList.size() > 20) {
                guessString = currList.back();
            }
            else {
                guessString = currList[0];
            }
            
            // if (prevSize == currList.size())
            // cout << currList[0] << " " << currList[1] << " " << currList[2]  << endl;
            // printf(" match: %d\n", guessMatch);
            // prevSize = currList.size()
        } 
                
    }
};