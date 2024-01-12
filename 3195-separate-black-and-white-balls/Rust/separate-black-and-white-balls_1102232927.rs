impl Solution {
    pub fn minimum_steps(s: String) -> i64 {
        let mut total = 0;
        let mut white_idx = 0;
        for (i, c) in s.chars().enumerate() {
            if c == '0' {
                total += (i-white_idx) as i64;
                white_idx += 1;
            }
        }
        total
    }
}