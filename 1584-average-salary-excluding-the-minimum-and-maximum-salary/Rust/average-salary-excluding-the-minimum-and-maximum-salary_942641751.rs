impl Solution {
    pub fn average(salary: Vec<i32>) -> f64 {
        let sum = salary.iter().fold(0, |mut sum, &val| {sum += val; sum});
        let min_value = salary.iter().min().unwrap();
        let max_value = salary.iter().max().unwrap();
        
        let res: f64 = (sum - min_value - max_value) as f64 / (salary.len() as i32 - 2) as f64;
        res
    }
}