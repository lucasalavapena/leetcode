pub const DIRS: [(i32, i32); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];


impl Solution {
    pub fn generate_matrix(n: i32) -> Vec<Vec<i32>> {
        let mut v: Vec<Vec<i32>> = vec![vec![0; n as usize]; n as usize];
        let mut curr: (i32, i32) = (0, 0);
        let mut curr_dir: usize = 0;

        for val in 1..=(n*n) {
            let (x, y) = curr;
            // println!("x: {x} y: {y} val:{val}");

            v[x as usize][y as usize] = val;
            let new_x = curr.0 + DIRS[curr_dir].0;
            let new_y = curr.1 + DIRS[curr_dir].1;
            if (new_x >= n || new_x < 0 || new_y >= n || new_y < 0 || v[new_x as usize][new_y as usize] != 0) {
                curr_dir = (curr_dir + 1) % 4;
            } 
            curr = (curr.0 + DIRS[curr_dir].0, curr.1 + DIRS[curr_dir].1);
        }
        return v;
    }
}