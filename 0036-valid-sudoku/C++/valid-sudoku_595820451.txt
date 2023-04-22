class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.' and not isValidSudoku(board, i, j)) {
                    return false;
                }
            }
        }
        
        for (int i = 0; i < 3; i++) {
           for (int j = 0; j < 3; j++) {
               if (not isSquareValid(board,i, j))
                   return false;
            } 
        }
        
        return true;
    }
    
    bool isValidSudoku(vector<vector<char>>& board, int idx, int idxy) {
        
        // horizontally?
        char val = board[idx][idxy];
            
        for (int j = 0; j < 9; j++) {
            if (board[idx][j] == val and j != idxy){
                return false;
            }
        }
        
        //vertically
        for (int i = 0; i < 9; i++) {
            if (board[i][idxy] == val and i != idx){
                return false;
            }
        }
        
        
        return true;
    }
                
    
    int isSquareValid(vector<vector<char>>& board, int idx, int idxy) {
        unordered_set<char> s;
        
        int x_idx = idx * 3;
        int y_idx = idxy * 3;
        
        for (int i = x_idx; i < x_idx+3; i++) {
           for (int j = y_idx; j < y_idx+3; j++) {
                if (board[i][j] != '.') {
                    if (s.find(board[i][j]) != s.end()) {
                        return false;
                    }
                    else {
                        s.insert(board[i][j]);
                    }
                }
            } 
        }
    
        return true;
    }
    
};