impl Solution {
    pub fn hammingWeight (n: u32) -> i32 {
        let mut cnt = 0; 
        let mut m = n; 
        while m > 0 {  
            if (m & 1) > 0 {
                cnt += 1;
            }
            m >>= 1; 
        }
        cnt
    }
}