struct MyHashMap {
    buffer: Vec<Option<i32>>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyHashMap {

    fn new() -> Self {
        Self {
            buffer: Vec::new(),
        }
    }
    
    fn put(&mut self, key: i32, value: i32) {
        let index = key as usize;
        if self.buffer.len() <= index {
            self.buffer.resize(index + 1, None);
            self.buffer[index] = Some(value);
        } else {
            self.buffer[index] = Some(value);
        }
    }
    
    fn get(&self, key: i32) -> i32 {
        let index = key as usize;
        if self.buffer.len() <= index {
            return -1;
        }
        self.buffer[index].unwrap_or(-1)
    }
    
    fn remove(&mut self, key: i32) {
        let index = key as usize;
        if self.buffer.len() <= index {
            return;
        }
        self.buffer[index] = None;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * let obj = MyHashMap::new();
 * obj.put(key, value);
 * let ret_2: i32 = obj.get(key);
 * obj.remove(key);
 */