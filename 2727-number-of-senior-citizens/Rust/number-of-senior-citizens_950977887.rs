impl Solution {
    pub fn count_seniors(details: Vec<String>) -> i32 {
        details.iter().filter(|detail| {
            detail[11..=12].parse::<i32>().unwrap() > 60
        })
        .count() as i32
    }
}