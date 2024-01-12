struct MyHashMap {
    buckets: Vec<Vec<(i32,i32)>>,
}

const N_BUCKETS: usize = 7193;

impl MyHashMap {

    fn new() -> Self {
        Self{ buckets: vec![vec![]; N_BUCKETS] }
    }

    fn hash(key: i32) -> usize {
        key as usize % N_BUCKETS
    }

    fn find_entry(&self, key: i32) -> (usize, Result<usize, usize>) {
        let bucket_idx = Self::hash(key);
        let bucket = &self.buckets[bucket_idx];
        let result = bucket.binary_search_by(|(k, v)| k.cmp(&key));
        (bucket_idx, result)
    }
    
    fn put(&mut self, key: i32, value: i32) {
        match self.find_entry(key) {
            (bucket_idx, Ok(index)) => self.buckets[bucket_idx][index] = (key, value),
            (bucket_idx, Err(index)) => self.buckets[bucket_idx].insert(index, (key, value)),
        }
    }
    
    fn get(&self, key: i32) -> i32 {
        let bucket = &self.buckets[Self::hash(key)];
        match bucket.binary_search_by(|(k, v)| k.cmp(&key)) {
            Ok(index) => bucket[index].1,
            Err(index) => -1,
        }
    }
    
    fn remove(&mut self, key: i32) {
        match self.find_entry(key) {
            (bucket_idx, Ok(index)) => { self.buckets[bucket_idx].remove(index); },
            _ => (),
        }
    }
}