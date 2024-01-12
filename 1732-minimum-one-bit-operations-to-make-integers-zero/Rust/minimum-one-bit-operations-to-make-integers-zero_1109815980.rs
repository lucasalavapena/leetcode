impl Solution {
    pub fn minimum_one_bit_operations(mut n:  i32) -> i32 {
        // https://oeis.org/A006068
        n ^= n >> 16;
        n ^= n >>  8;
        n ^= n >>  4;
        n ^= n >>  2;
        n ^= n >>  1;
        n
    }
}