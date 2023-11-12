use std::collections::BinaryHeap;

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut heap = BinaryHeap::from(stones);
        let mut y: i32;
        let mut x: i32;
        while heap.len() > 1 {
            y = heap.pop().unwrap(); 
            x = heap.pop().unwrap(); 
            if y > x {
                heap.push(y-x);
            }
        }
        return heap.pop().unwrap_or(0); 

    }
}