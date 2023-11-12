use std::collections::HashMap;

struct FrequencyTracker {
    numbers: HashMap<i32, i32>,
    frequency: HashMap<i32, i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FrequencyTracker {

    fn new() -> Self {
        Self {
            numbers: HashMap::new(),
            frequency: HashMap::new(),
        }
    }

    fn update(&mut self, number: i32, dir: i32) {
        let old_freq = self.numbers[&number];
        *self.frequency.entry(old_freq).or_insert(0) += -1;
        *self.numbers.entry(number).or_insert(0) += dir;
        *self.frequency.entry(old_freq + dir).or_insert(0) += 1;
    }
    
    fn add(&mut self, number: i32) {
        // println!("add {number}");

        if self.numbers.contains_key(&number) {
            self.update(number, 1);
        }
        else {
            *self.frequency.entry(1).or_insert(0) += 1;
            self.numbers.insert(number, 1);
        }
    }
    
    fn delete_one(&mut self, number: i32) {
        // println!("delete_one {number}");

        if self.numbers.contains_key(&number) && self.numbers[&number] > 0 {
            self.update(number, -1);
        }
    }
    
    fn has_frequency(&self, frequency: i32) -> bool {        
        // println!("frequency: {:?}", self.frequency);
        // println!("numbers: {:?}", self.numbers);

        self.frequency.contains_key(&frequency) && self.frequency[&frequency] > 0
    }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * let obj = FrequencyTracker::new();
 * obj.add(number);
 * obj.delete_one(number);
 * let ret_3: bool = obj.has_frequency(frequency);
 */