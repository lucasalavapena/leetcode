impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut max1 = nums[0].min(nums[1]);
        let mut max2 = nums[0].max(nums[1]);
        for i in 2..nums.len() {
            if max2 < nums[i] {
                max1 = max2;
                max2 = nums[i];
            }
            else if max1 < nums[i] {
                max1 = nums[i];
            }
        }
        (max1-1) * (max2-1)
    }
}