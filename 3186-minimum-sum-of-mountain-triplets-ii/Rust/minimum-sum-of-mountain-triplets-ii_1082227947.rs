impl Solution {
    pub fn minimum_sum(nums: Vec<i32>) -> i32 {
        let min_so_far = i32::MAX;

        let min_left: Vec<i32> = nums.iter().scan(min_so_far, |min, &x| {
            *min = std::cmp::min(*min, x);
            Some(*min)
        }).collect();

        let min_right: Vec<i32> = nums.iter().rev().scan(min_so_far, |min, &x| {
            *min = std::cmp::min(*min, x);
            Some(*min)
        })        .collect::<Vec<_>>() // Collect into a vector
        .iter()
        .rev()
        .cloned() // Add .cloned() to get a vector of i32
        .collect();
        // println!("{min_left:?}");
        // println!("{min_right:?}");

        let mut res = i32::MAX;

        for (i, n) in nums.iter().enumerate() {
            if i == 0 || i == nums.len() - 1 {
                continue;
            }
            if min_left[i-1] < *n && min_right[i + 1] < *n {
                let curr =  min_left[i-1] + n + min_right[i + 1];
                res = std::cmp::min(res, curr);
            }

        }

        if (res == i32::MAX) {
            return -1;
        }
        return res;
    }
}