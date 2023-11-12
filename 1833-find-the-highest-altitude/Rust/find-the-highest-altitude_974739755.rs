impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut highest_altitude = 0;
        
        gain.into_iter().fold(0, |mut acc, x| {
            acc += x;
            highest_altitude = highest_altitude.max(acc);
            acc
        });

        highest_altitude
    }
}