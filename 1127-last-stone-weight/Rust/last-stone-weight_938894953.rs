use std::collections::BinaryHeap;

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut heap = BinaryHeap::from(stones);

        let mut y: i32;
        let mut x: i32;

        while heap.len() > 1 {
            y = heap.pop().unwrap(); 
            x = heap.pop().unwrap(); 
            if x == y {
                continue;
            } else {
                heap.push(y-x);
            }

        }
        let res = heap.pop();
        if res.is_none() {
            return 0;
        }
        return res.unwrap();

    }
}