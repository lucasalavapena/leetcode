use std::collections::BinaryHeap;

struct KthLargest {
    h: BinaryHeap<i32>,
    k: usize,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl KthLargest {

    fn new(k: i32, nums: Vec<i32>) -> Self {

        let neg_nums = nums.iter().map(|n| -n).collect::<Vec<i32>>();
        let mut heap = BinaryHeap::from(neg_nums);
        
        let k_usize = k as usize;

        while heap.len() > k_usize {
            heap.pop();
        }

        Self {
            h: heap,
            k: k_usize, 
        }
    }
    
    fn add(&mut self, val: i32) -> i32 {
        self.h.push(-val);
        if self.h.len() > self.k {
            self.h.pop();
        }
        -self.h.peek().unwrap()
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * let obj = KthLargest::new(k, nums);
 * let ret_1: i32 = obj.add(val);
 */