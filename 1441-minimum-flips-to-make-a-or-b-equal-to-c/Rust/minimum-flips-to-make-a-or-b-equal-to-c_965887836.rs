impl Solution {
    pub fn min_flips(a: i32, b: i32, c: i32) -> i32 {
        let mut res = 0;
        for i in 0..32 {
            let a_bit = a & (1 << i) != 0;
            let b_bit = b & (1 << i) != 0;
            let c_bit = c & (1 << i) != 0;
            // println!("{a_bit} {b_bit} {c_bit} {res}");
            if (a_bit | b_bit) == c_bit {
                continue;
            }
            if a_bit  && b_bit  && !c_bit {
                res += 2
            }
            else {
                res += 1
            }
        }
        res
    }
}