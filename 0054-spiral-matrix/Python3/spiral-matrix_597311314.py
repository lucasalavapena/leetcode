class Solution:
    def is_in_bounds(self, pos):
        if pos[0] < 0 or self.matrix_size[0] <= pos[0] or pos[1] < 0 or self.matrix_size[1] <= pos[1]:
            return False
        return True
    
    def move(self, curr_pos, direction):
        return (curr_pos[0] + direction[0], curr_pos[1] + direction[1])
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    
        
        self.matrix_size = (len(matrix[0]), len(matrix))
        
        if self.matrix_size[0] == 1 and self.matrix_size[1] == 1:
            return matrix[0]
            
        
        visited = [0 for j in range(self.matrix_size[0]) for i in range(self.matrix_size[1])]
        # print(visited)
        
        directions = [
                        (1, 0),
                        (0, 1),
                        (-1, 0),
                        (0, -1)
                    ]
        res = [matrix[0][0]]
        visited[0] = 1
        curr_pos = (0, 0)
        i = 0
        while True:
            

            next_move = self.move(curr_pos, directions[i % 4])
            x_move, y_move = next_move

            # print(f"{curr_pos=} {next_move=}")
#             if i == 3:
#                 return res
            
            if self.is_in_bounds(next_move) and not visited[x_move + self.matrix_size[0] * y_move]:
                # print(f"{visited=} {all(visited)=}")
                res.append(matrix[y_move][x_move])
                visited[x_move + self.matrix_size[0] * y_move] = 1
                curr_pos = next_move
                
                if all(visited):
                    return res

            else:
                i += 1
                
            
             
 
        
        