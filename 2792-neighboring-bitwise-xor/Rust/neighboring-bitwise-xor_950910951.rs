impl Solution {
    pub fn does_valid_array_exist(derived: Vec<i32>) -> bool {
       derived.iter().sum::<i32>() % 2 == 0 
    }
}