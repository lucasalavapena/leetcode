impl Solution {
    pub fn find_champion(grid: Vec<Vec<i32>>) -> i32 {
        let mut champion = 0;
        for j in 1..grid.len(){
            if grid[champion][j] == 0 {
                champion = j;
            }
        }
        champion as i32
    }
}