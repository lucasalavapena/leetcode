impl Solution {
    pub fn average(salary: Vec<i32>) -> f64 {
        let [sum, min_value, max_value] = salary.iter().fold([0, i32::MAX, i32::MIN], |mut data, &val| {
                data[0] += val; 
                data[1] = std::cmp::min(val, data[1]);
                data[2] = std::cmp::max(val, data[2]);
                data
            });
        
        let res: f64 = (sum - min_value - max_value) as f64 / (salary.len() as i32 - 2) as f64;
        res
    }
}