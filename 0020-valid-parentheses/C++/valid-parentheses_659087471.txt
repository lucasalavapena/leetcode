class Solution {
public:
    map<char, int> char2Type {
                {'(', 1},
                {')', 1},
                {'{', 2},
                {'}', 2},
                {'[', 3},
                {']', 3},
    };
    
    map<int, int> typeCounter {
                {1, 0},
                {2, 0},
                {3, 0},
    };
    
//     int getType(char subS) {
//             if (subS == '(' || subS == ')') {
//                 return
    // 1;
//             }
//             if (subS == '[' || subS == ']') {
//                 return 2;
//             }            
//             if (subS == '{' || subS == '}') {
//                 return 3;
//             }
//         return -1;
//     }
    
    bool isValid(string s) {
        int type = 0;
        vector<int> type2Finish;

        // 1: () 2: [] 3: {}
        
        for (char subS: s) {
            type = char2Type[subS];
            
            
            if (subS == '(' || subS == '[' || subS == '{') {
                typeCounter[type]++;
                type2Finish.push_back(type); 
            }
            else {
                typeCounter[type]--;
                if (type2Finish.empty())
                    return false;
                if (type == type2Finish.back()) {
                    type2Finish.pop_back();
                }
                else {
                    return false;
                }
            }
            
            // if (type == type2Finish.back()) {
            //     type2Finish.pop_back();
            // }
            // else {
            //     type2Finish.push_back(type); 
            // }
            
//             if () {
//                 continue;
// //             }
//             if ()
//             if (typeCounter[type] <= 0 && typeCounter[type2Finish.back()] != 0) {
//                 return false;
//             }
            // printf("%c %d %d\n", subS, type2Finish, type);

            // type2Finish = type;

                        
        }
        
        if (typeCounter[1] != 0 || typeCounter[2] != 0 || typeCounter[3] != 0)
            return false;
        
        return true;
    }
};