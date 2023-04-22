impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut low = 0 as i32;
        let mut high = (nums.len()-1) as i32;

        while low <= high {
            let mid = ((low + high) / 2) ;
            if nums[mid as usize] == target {
                return mid;
            } else if nums[mid as usize] < target {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }
}