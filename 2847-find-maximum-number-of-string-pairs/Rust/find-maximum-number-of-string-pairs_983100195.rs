use std::collections::HashSet;

impl Solution {
    pub fn maximum_number_of_string_pairs(words: Vec<String>) -> i32 {
        let mut count = 0;
        let mut set = HashSet::new();

        for word in words {
            let reversed_word: String = word.chars().rev().collect();
            if set.contains(&reversed_word) {
                count += 1;
                set.remove(&reversed_word);
            } else {
                set.insert(word);
            }
        }

        count
    }
}