impl Solution {
    pub fn max_strength(nums: Vec<i32>) -> i64 {
        let neg: Vec<i64> = nums.iter()
                                .filter(|&n| n < &0)
                                .map(|n| *n as i64)
                                .collect();

        let pos: Vec<i64> = nums.iter()
                                .filter(|&n| n > &0)
                                .map(|n| *n as i64)
                                .collect();

        if neg.len() == 0 && pos.len() == 0 {
            return 0;
        }
        let prod = |nums: &Vec<i64>| nums.iter().fold(1, |acc, &x| acc * x);
        let res = prod(&neg) * prod(&pos);

        // need to remove the largest negative number (closest to zero from the negative side) used
        if neg.len() % 2 == 1 {
            if neg.len() == 1 && pos.len() == 0 {
                // some zeros exist in the input
                if nums.len() > 1 {
                    return 0
                }
                else {
                    return neg[0];
                }
            }
            let max_neg = neg.iter().max().unwrap();
            return res/max_neg;
        }
        return res;
    }
}