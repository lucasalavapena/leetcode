impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        gain.into_iter().fold((0, 0), |(res , h), g| (
            (res.max(h + g), h + g)
        )).0
    }
}