use std::collections::VecDeque;

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut q = VecDeque::from([0]);
        let k_usize = k as usize;
        let mut res = vec![0; nums.len()-k_usize+1];

        for i in 0..nums.len() {
            
            while !q.is_empty() && i >= k_usize && i - k_usize >= *q.front().unwrap() {
                q.pop_front();
            }

            while !q.is_empty() && nums[i] >= nums[*q.back().unwrap()]  {
                q.pop_back();
            }
            q.push_back(i);

            if i >= k_usize - 1 {
                res[i-(k_usize - 1)] = nums[*q.front().unwrap()];
            }
        }
        res

    }
}