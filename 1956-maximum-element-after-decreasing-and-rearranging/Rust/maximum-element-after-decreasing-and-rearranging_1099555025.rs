impl Solution {
    pub fn maximum_element_after_decrementing_and_rearranging(arr: Vec<i32>) -> i32 {
        let mut arr_ = arr.clone();
        arr_.sort();
        let mut prev = 1;
        for i in 1..arr_.len() {
            prev = arr_[i].min(prev + 1);
        }
        prev
    }
}