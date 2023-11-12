impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n <= 3 {
            return n;
        }
        let mut curr = 0;
        let mut prev = 3;
        let mut prevprev = 2;

        for i in 3..n {
            curr = prev + prevprev;
            prevprev = prev;
            prev = curr;
            // (prev, prevprev) = (curr, prev);
        }
        return curr;
    }
}