impl Solution {
    pub fn is_power_of_four(n: i32) -> bool {
        n.count_ones() == 1 && n.trailing_zeros() % 2 == 0
    }
}