impl Solution {
    pub fn maximum_element_after_decrementing_and_rearranging(mut arr: Vec<i32>) -> i32 {
        arr.sort();
        let mut prev = 1;
        for i in 1..arr.len() {
            prev = arr[i].min(prev + 1);
        }
        prev
    }
}