impl Solution {
    pub fn find_array(pref: Vec<i32>) -> Vec<i32> {
        pref.iter().fold((0, Vec::new()), |(prev_pref, mut res), &p| {
            res.push(p ^ prev_pref);
            (p, res)
        }).1
    }
}