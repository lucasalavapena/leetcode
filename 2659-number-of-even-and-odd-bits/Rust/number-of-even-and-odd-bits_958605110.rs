impl Solution {
    pub fn even_odd_bit(n: i32) -> Vec<i32> {
        let mut odd = 0;
        let mut even =  0;

        for i in 0..32 {
            if i % 2 == 0 {
                even += (n & (1 << i) != 0 ) as i32;
            }
            else {
                odd += (n & (1 << i) != 0 ) as i32;
            }
        }
        vec![even, odd]
    }
}