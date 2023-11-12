impl Solution {
    pub fn find_array(pref: Vec<i32>) -> Vec<i32> {
        let mut prev_pref = 0;
        let mut res: Vec<i32>  = Vec::with_capacity(pref.len());
        
        for p in pref {
            res.push(p ^ prev_pref);
            prev_pref = p;
        }
        res
    }
}