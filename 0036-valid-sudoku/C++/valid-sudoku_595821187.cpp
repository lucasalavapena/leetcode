class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
vector<set<int>> rows(9), cols(9), blocks(9);
        
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                
                if (board[i][j] == '.') continue;
                
                int curr = board[i][j] - '0';
                if (rows[i].count(curr) || cols[j].count(curr) || blocks[(i/3)*3+j/3].count(curr)) 
                    return false;
                
                rows[i].insert(curr);
                cols[j].insert(curr);
                blocks[(i/3)*3+j/3].insert(curr);
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