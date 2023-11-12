use std::collections::VecDeque;

struct RecentCounter {
    calls: VecDeque<i32>,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RecentCounter {

    fn new() -> Self {
        Self{calls: VecDeque::new()}
    }
    
    fn ping(&mut self, t: i32) -> i32 {
        self.calls.push_back(t);

        while *self.calls.front().unwrap() < t - 3_000 {
            self.calls.pop_front();
        }

        self.calls.len() as i32
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * let obj = RecentCounter::new();
 * let ret_1: i32 = obj.ping(t);
 */