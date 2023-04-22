impl Solution {
    pub fn row_and_maximum_ones(mat: Vec<Vec<i32>>) -> Vec<i32> {
        let mut max_idx: i32 = 0;
        let mut max_count: i32 = 0;
        let mut row_count: i32;

        for (i, row) in (&mat).iter().enumerate() {
            row_count = row.iter().filter(|&n| *n == 1).count() as i32;
            if row_count > max_count {
                max_count = row_count;
                max_idx = i as i32;
            }
        }
        vec![max_idx, max_count]
    }
}