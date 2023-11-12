impl Solution {
    pub fn maximize_sum(nums: Vec<i32>, k: i32) -> i32 {
        k * nums.iter().max().unwrap() + (k - 1) * k/2
    }
}