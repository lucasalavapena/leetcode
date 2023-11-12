impl Solution {
    pub fn sum_of_multiples(n: i32) -> i32 {
        (3..=n).filter(|n| n % 3 == 0 || n % 5 == 0 || n % 7 == 0).sum()
    }
}